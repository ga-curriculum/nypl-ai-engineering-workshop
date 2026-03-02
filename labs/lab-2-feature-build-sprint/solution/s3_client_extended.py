"""
Reference solution for Lab 2: Feature Build Sprint

This file shows the complete S3Client with all three tiers implemented.
Copy this into python-utils/src/nypl_py_utils/classes/s3_client.py to use it.
"""

import boto3
import csv
import json
import os

from botocore.exceptions import ClientError
from io import BytesIO, StringIO
from nypl_py_utils.functions.log_helper import create_log


class S3Client:
    """
    Client for interacting with AWS S3 files.

    Takes as input the name of the S3 bucket and an optional resource
    (object key) to be fetched/set.
    """

    # --- Stretch tier: resource is now optional ---
    def __init__(self, bucket, resource=None):
        self.logger = create_log('s3_client')
        self.bucket = bucket
        self.resource = resource

        try:
            self.s3_client = boto3.client(
                's3', region_name=os.environ.get('AWS_REGION', 'us-east-1'))
        except ClientError as e:
            self.logger.error(
                'Could not create S3 client: {err}'.format(err=e))
            raise S3ClientError(
                'Could not create S3 client: {err}'.format(err=e)) from None

    def _require_resource(self):
        """Raise if no resource was specified in the constructor."""
        if self.resource is None:
            raise S3ClientError('No resource specified')

    def close(self):
        self.s3_client.close()

    def fetch_cache(self):
        """Fetches a JSON file from S3 and returns the resulting dictionary"""
        self._require_resource()
        self.logger.info('Fetching {file} from S3 bucket {bucket}'.format(
            file=self.resource, bucket=self.bucket))
        try:
            output_stream = BytesIO()
            self.s3_client.download_fileobj(
                self.bucket, self.resource, output_stream)
            return json.loads(output_stream.getvalue())
        except ClientError as e:
            self.logger.error(
                'Error retrieving {file} from S3 bucket {bucket}: {error}'
                .format(file=self.resource, bucket=self.bucket, error=e))
            raise S3ClientError(
                'Error retrieving {file} from S3 bucket {bucket}: {error}'
                .format(file=self.resource, bucket=self.bucket, error=e)
            ) from None

    def set_cache(self, state):
        """Writes a dictionary to JSON and uploads the resulting file to S3"""
        self._require_resource()
        self.logger.info(
            'Setting {file} in S3 bucket {bucket} to {state}'.format(
                file=self.resource, bucket=self.bucket, state=state))
        try:
            input_stream = BytesIO(json.dumps(state).encode())
            self.s3_client.upload_fileobj(
                input_stream, self.bucket, self.resource)
        except ClientError as e:
            self.logger.error(
                'Error uploading {file} to S3 bucket {bucket}: {error}'
                .format(file=self.resource, bucket=self.bucket, error=e))
            raise S3ClientError(
                'Error uploading {file} to S3 bucket {bucket}: {error}'
                .format(file=self.resource, bucket=self.bucket, error=e)
            ) from None

    # --- Base tier ---
    def list_objects(self, prefix=None):
        """
        Lists object keys in the S3 bucket.

        Parameters
        ----------
        prefix : str, optional
            If provided, only keys starting with this prefix are returned.

        Returns
        -------
        list of str
            A list of object key strings.
        """
        self.logger.info(
            'Listing objects in S3 bucket {bucket}{pfx}'.format(
                bucket=self.bucket,
                pfx=' with prefix "{}"'.format(prefix) if prefix else ''))
        try:
            kwargs = {'Bucket': self.bucket}
            if prefix is not None:
                kwargs['Prefix'] = prefix
            response = self.s3_client.list_objects_v2(**kwargs)
            return [obj['Key'] for obj in response.get('Contents', [])]
        except ClientError as e:
            self.logger.error(
                'Error listing objects in S3 bucket {bucket}: {error}'
                .format(bucket=self.bucket, error=e))
            raise S3ClientError(
                'Error listing objects in S3 bucket {bucket}: {error}'
                .format(bucket=self.bucket, error=e)
            ) from None

    # --- Intermediate tier ---
    def fetch_csv(self):
        """
        Downloads a CSV file from S3 and returns a list of dictionaries.

        Each dictionary represents one row, with the header row used as keys.
        All values are strings (no type conversion).

        Returns
        -------
        list of dict
            One dictionary per CSV row.
        """
        self._require_resource()
        self.logger.info('Fetching CSV {file} from S3 bucket {bucket}'.format(
            file=self.resource, bucket=self.bucket))
        try:
            output_stream = BytesIO()
            self.s3_client.download_fileobj(
                self.bucket, self.resource, output_stream)
            csv_text = output_stream.getvalue().decode('utf-8')
            reader = csv.DictReader(StringIO(csv_text))
            return list(reader)
        except ClientError as e:
            self.logger.error(
                'Error retrieving CSV {file} from S3 bucket {bucket}: {error}'
                .format(file=self.resource, bucket=self.bucket, error=e))
            raise S3ClientError(
                'Error retrieving CSV {file} from S3 bucket {bucket}: {error}'
                .format(file=self.resource, bucket=self.bucket, error=e)
            ) from None

    # --- Stretch tier ---
    def delete_cache(self):
        """Deletes the current resource from the S3 bucket."""
        self._require_resource()
        self.logger.info('Deleting {file} from S3 bucket {bucket}'.format(
            file=self.resource, bucket=self.bucket))
        try:
            self.s3_client.delete_object(
                Bucket=self.bucket, Key=self.resource)
        except ClientError as e:
            self.logger.error(
                'Error deleting {file} from S3 bucket {bucket}: {error}'
                .format(file=self.resource, bucket=self.bucket, error=e))
            raise S3ClientError(
                'Error deleting {file} from S3 bucket {bucket}: {error}'
                .format(file=self.resource, bucket=self.bucket, error=e)
            ) from None


class S3ClientError(Exception):
    def __init__(self, message=None):
        self.message = message
