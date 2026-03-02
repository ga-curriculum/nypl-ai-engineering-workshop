# Lab 2: Feature Build Sprint

## Overview

| Detail | Info |
|---|---|
| **Duration** | 35 minutes |
| **Tools** | Google Gemini Code Assist + GitHub Copilot |
| **Module** | Module 2: Working with Existing Codebases |
| **QA Persona** | Edge Case Hunter |
| **Depends On** | python-utils clone (see [sandbox/README.md](../../sandbox/README.md)) |
| **Target File** | `python-utils/src/nypl_py_utils/classes/s3_client.py` |

## Objective

Build a new feature in the `S3Client` class using the dual-tool workflow: Gemini Code Assist for planning and task decomposition, Copilot for implementation.

## Before You Start

Make sure you've cloned and set up python-utils:
```bash
cd python-utils
source venv/bin/activate
python -m pytest tests/test_s3_client.py -v   # Should see 2 tests pass
```

## Instructions

### Base Tier (2-5 years experience)

1. Read the feature spec in [`starter/feature-spec.md`](starter/feature-spec.md)
2. Open `s3_client.py` in VS Code and use Gemini Code Assist to decompose the `list_objects` feature into implementation steps
3. Implement `list_objects(prefix=None)` using Copilot inline suggestions
4. Run the existing tests to verify you haven't broken anything: `python -m pytest tests/test_s3_client.py -v`
5. Apply the Edge Case Hunter persona (see [`review/review-checklist.md`](review/review-checklist.md)) to your new code

### Intermediate Tier (5-15 years experience)

All of the above, plus:
6. Implement `fetch_csv()` — downloads a CSV and returns a list of dicts
7. Ask Gemini Code Assist to identify edge cases specific to your CSV parsing
8. Write tests for at least 3 edge cases Gemini Code Assist identifies

### Stretch Tier (15-25 years experience)

All of the above, plus:
9. Add `delete_cache()` and refactor the constructor to make `resource` optional
10. Implement resource validation — methods that need `resource` should raise `S3ClientError` if it's `None`
11. Use Gemini Code Assist to evaluate your task decomposition: "Was this the right breakdown?"

## Codebase

This lab uses NYPL's **python-utils** library. See [`sandbox/README.md`](../../sandbox/README.md) for clone instructions and setup.

**Key files:**
- Source: `python-utils/src/nypl_py_utils/classes/s3_client.py` (~65 lines)
- Tests: `python-utils/tests/test_s3_client.py` (2 existing tests)

## Running Tests

```bash
# From the python-utils directory
python -m pytest tests/test_s3_client.py -v
```

## Important

Make sure `s3_client.py` is in a working state and all existing tests still pass before moving on. If you're stuck, use the reference solution in [`solution/s3_client_extended.py`](solution/s3_client_extended.py).

**Note:** Lab 3 uses the *original* `s3_client.py` (not your extensions), so you can proceed to Lab 3 even if you didn't finish all tiers here.

## Review Step

Apply the Edge Case Hunter checklist in [`review/review-checklist.md`](review/review-checklist.md) before considering this lab complete.
