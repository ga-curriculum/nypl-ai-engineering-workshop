# Lab 3: AI Test Suite

## Overview

| Detail | Info |
|---|---|
| **Duration** | 30 minutes |
| **Tools** | Google Gemini Code Assist + GitHub Copilot |
| **Module** | Module 3: Testing and QA with AI |
| **QA Persona** | Test Coverage Analyst |
| **Depends On** | python-utils clone (see [sandbox/README.md](../../sandbox/README.md)) |
| **Target File** | `python-utils/src/nypl_py_utils/classes/s3_client.py` (the *original*, not Lab 2 extensions) |

## Objective

Critically evaluate AI-generated tests for the `S3Client` class. Learn to spot hallucinated assertions — tests that look correct but assert behavior the code doesn't have.

## Before You Start

Make sure python-utils is set up and tests pass:
```bash
cd python-utils
source venv/bin/activate
python -m pytest tests/test_s3_client.py -v   # Should see 2 tests pass
```

## Instructions

### Base Tier (2-5 years experience)

1. Copy [`starter/test_s3_client_review.py`](starter/test_s3_client_review.py) into your `python-utils/tests/` directory
2. Open `s3_client.py` side-by-side with the test file — read each test against the source
3. Run the tests: `python -m pytest tests/test_s3_client_review.py -v`
4. Identify which tests **fail** — these are candidates for hallucinations
5. For each failing test, explain: what does the test assume, and why doesn't the code do that?
6. Apply the Test Coverage Analyst persona (see [`review/review-checklist.md`](review/review-checklist.md))

### Intermediate Tier (5-15 years experience)

All of the above, plus:
7. Use Gemini Code Assist to analyze the test suite: "What's NOT tested in this suite?"
8. Write tests for 3 gaps Gemini Code Assist identifies
9. Ask Gemini Code Assist: "Are any of these tests tautological?" — verify its findings

### Stretch Tier (15-25 years experience)

All of the above, plus:
10. Generate a new test suite with Copilot, then a separate one with Gemini Code Assist — compare quality
11. Create a test quality scorecard: rate each test on specificity, coverage, and correctness
12. Write a "test review" prompt that you'd use in your own workflow going forward

## The Hallucinated Test Exercise

The file [`starter/test_s3_client_review.py`](starter/test_s3_client_review.py) contains **10 "AI-generated" tests** for the *original* `S3Client` class (the version already in the repo — not your Lab 2 extensions).

Three of these tests are **hallucinated** — they assert behavior that does not exist in `s3_client.py`. Your job is to:
1. Identify which 3 tests are hallucinated
2. Explain what each hallucinated test assumes
3. Categorize the hallucination type (assumed feature, assumed error handling, invented capability)

When you're done, check your answers against [`solution/hallucination-answers.md`](solution/hallucination-answers.md).

## Codebase

This lab targets the **original** `s3_client.py` in python-utils — the version with `fetch_cache()` and `set_cache()` only. You do not need to have completed Lab 2 to do this lab.

**Key files:**
- Source: `python-utils/src/nypl_py_utils/classes/s3_client.py` (~65 lines)
- Existing tests: `python-utils/tests/test_s3_client.py` (2 tests — note the sparse coverage)
- Hallucinated test file: `starter/test_s3_client_review.py` (copy this into `python-utils/tests/`)

## Running Tests

```bash
# From the python-utils directory
python -m pytest tests/test_s3_client_review.py -v
```

## Cleanup

The copied review file is intentionally designed to fail 3 tests. After the exercise, remove `python-utils/tests/test_s3_client_review.py` (or revert your sandbox) before running the full `python-utils` test suite again.

## Review Step

Apply the Test Coverage Analyst checklist in [`review/review-checklist.md`](review/review-checklist.md). The key question: "If all tests pass, am I confident the code works correctly?"
