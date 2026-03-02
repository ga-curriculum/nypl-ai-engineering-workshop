# Feature Spec: Extend S3Client

## Context

Open `src/nypl_py_utils/classes/s3_client.py` in the python-utils repo. The `S3Client` class currently supports two operations:

- `fetch_cache()` — downloads a JSON file from S3 and returns a dictionary
- `set_cache(state)` — uploads a dictionary as a JSON file to S3

Your task is to extend `S3Client` with new capabilities. Use the **dual-tool workflow**: Gemini Code Assist for planning and task decomposition, Copilot for implementation.

## Target File

```
python-utils/src/nypl_py_utils/classes/s3_client.py
```

## Existing Tests

```
python-utils/tests/test_s3_client.py
```

Run existing tests before and after your changes to make sure nothing breaks:
```bash
python -m pytest tests/test_s3_client.py -v
```

---

## Base Tier

### Add `list_objects(prefix=None)`

Add a method that lists object keys in the S3 bucket.

**Behavior:**
- If `prefix` is `None`, list all objects in the bucket
- If `prefix` is provided, list only objects whose keys start with that prefix
- Return a list of key strings (e.g., `["data/file1.json", "data/file2.json"]`)
- Use `self.s3_client.list_objects_v2(Bucket=self.bucket)` (add `Prefix=prefix` when provided)
- The response dict has a `'Contents'` key containing a list of objects, each with a `'Key'` field
- If the bucket is empty or the prefix matches nothing, return an empty list
- Raise `S3ClientError` on `ClientError`

**Example usage:**
```python
client = S3Client('my-bucket', 'my-resource')
all_keys = client.list_objects()                  # ["file1.json", "data/file2.json"]
data_keys = client.list_objects(prefix='data/')   # ["data/file2.json"]
```

---

## Intermediate Tier

All of the Base tier, plus:

### Add `fetch_csv()`

Add a method that downloads a CSV file from S3 and returns it as a list of dictionaries (one dict per row, using the header row as keys).

**Behavior:**
- Download the file at `self.resource` from `self.bucket` (same pattern as `fetch_cache`)
- Decode the bytes as UTF-8
- Parse the CSV content using Python's `csv.DictReader`
- Return a list of dicts (e.g., `[{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]`)
- Raise `S3ClientError` on `ClientError`

**Hints:**
- You'll need `import csv` and `from io import StringIO`
- `csv.DictReader` takes a file-like object — wrap the decoded string in `StringIO`
- Remember: CSV values are always strings (don't try to convert types)

---

## Stretch Tier

All of the above, plus:

### Add `delete_cache()`

Add a method that deletes the current resource from the S3 bucket.

**Behavior:**
- Delete the object at `self.resource` in `self.bucket`
- Use `self.s3_client.delete_object(Bucket=self.bucket, Key=self.resource)`
- Log the operation (follow the logging pattern of existing methods)
- Raise `S3ClientError` on `ClientError`

### Refactor constructor to make `resource` optional

Modify `__init__` so that `resource` defaults to `None`. This makes `S3Client` usable as a bucket-level client (for `list_objects`) without requiring a specific resource path.

**Rules:**
- `resource` should default to `None`
- Methods that require `resource` (`fetch_cache`, `set_cache`, `fetch_csv`, `delete_cache`) should raise `S3ClientError` with message `'No resource specified'` if `self.resource` is `None`
- `list_objects` should work regardless of whether `resource` is set
- Existing tests must still pass (they provide `resource` in the constructor)

---

## Workflow Reminder

1. **Plan first:** Ask Gemini Code Assist to decompose your chosen tier into implementation steps
2. **Implement:** Use Copilot inline suggestions to write the code
3. **Test:** Run `python -m pytest tests/test_s3_client.py -v` after each change
4. **Review:** Apply the Edge Case Hunter persona (see `review/review-checklist.md`)
