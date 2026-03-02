# Sandbox — NYPL python-utils

The workshop labs use NYPL's **python-utils** library as the "existing codebase" that participants analyze, extend, test, and review with AI tools.

The codebase lives in a separate repository. You will clone it alongside this workshop repo — **do not copy it into this directory**.

## Quick Start

```bash
# 1. Clone the python-utils repo (alongside this workshop repo)
git clone https://github.com/NYPL-GA-Training/python-utils.git
cd python-utils

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install all dependencies (includes boto3, pytest, mocks — everything you need)
pip install '.[development]'

# 4. Run the test suite to verify setup
python -m pytest
```

You should see all 103 tests pass. If they do, you're ready for the labs.

## No AWS Credentials Needed

The python-utils codebase wraps AWS services (S3, KMS, Secrets Manager, etc.), but **all tests use mocks** — no AWS account or credentials are required. The `.[development]` install includes `pytest-mock`, `mock`, and `requests-mock` so everything runs locally.

## What's in python-utils?

```
python-utils/
├── src/nypl_py_utils/
│   ├── classes/
│   │   ├── s3_client.py           ← Labs 2 & 3 target this file
│   │   ├── kms_client.py          ← Capstone targets this file
│   │   ├── secrets_manager_client.py
│   │   ├── kinesis_client.py
│   │   └── ...                    (10+ client modules)
│   └── functions/
│       ├── log_helper.py
│       ├── config_helper.py
│       └── ...
├── tests/
│   ├── test_s3_client.py          ← Only 2 tests (good bridge to Lab 3)
│   ├── test_kms_client.py
│   └── ...                        (one test file per module)
└── pyproject.toml
```

## How Labs Use This Codebase

| Lab | File | Task |
|---|---|---|
| Lab 2: Feature Build Sprint | `s3_client.py` | Add new methods (list, CSV fetch, cache management) |
| Lab 3: AI Test Suite | `test_s3_client.py` | Evaluate AI-generated tests for hallucinations |
| Capstone | `kms_client.py` | Add encryption + secret rotation |

## Running Tests

```bash
# Run all tests
python -m pytest

# Run tests for a specific module
python -m pytest tests/test_s3_client.py -v

# Run with verbose output
python -m pytest -v
```

## Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: nypl_py_utils` | Make sure you ran `pip install '.[development]'` (not just `pip install .`) |
| `pip install` fails on `psycopg` | This is a postgres driver — try `pip install '.[development]'` again, or install `libpq-dev` on Linux |
| Tests fail with import errors | Ensure your virtual environment is activated (`source venv/bin/activate`) |
| `python` not found | Try `python3` instead |
