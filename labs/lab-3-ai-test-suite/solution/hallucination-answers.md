# Hallucination Answer Key

## Summary

Of the 10 tests in `test_s3_client_review.py`, **3 are hallucinated** (Tests 4, 7, and 9). The other 7 tests correctly assert real behavior of the `S3Client` class.

---

## Valid Tests

| Test | What It Tests | Why It's Valid |
|---|---|---|
| **Test 1** | `fetch_cache` returns parsed JSON | Matches the `json.loads(output_stream.getvalue())` in the source |
| **Test 2** | `set_cache` uploads serialized JSON | Matches the `json.dumps(state).encode()` + `upload_fileobj` pattern |
| **Test 3** | `fetch_cache` raises `S3ClientError` on `ClientError` | The `except ClientError` block explicitly raises `S3ClientError` |
| **Test 5** | `set_cache` raises `S3ClientError` on `ClientError` | Same pattern — `except ClientError` wraps and re-raises |
| **Test 6** | Constructor stores `bucket` and `resource` | `self.bucket = bucket` and `self.resource = resource` are in `__init__` |
| **Test 8** | `set_cache` handles empty dict | `json.dumps({})` produces `"{}"` — nothing special-cases empty input |
| **Test 10** | `fetch_cache` uses correct bucket/resource | `download_fileobj(self.bucket, self.resource, output_stream)` passes both |

---

## Hallucinated Tests

### Test 4: `test_fetch_cache_retries_on_timeout`

**What it asserts:** `fetch_cache` retries up to 3 times when a `RequestTimeout` `ClientError` occurs.

**Why it's hallucinated:** The `fetch_cache` method has **no retry logic**. It catches `ClientError` exactly once and immediately raises `S3ClientError`. There is no loop, no retry counter, and no special handling for timeout errors vs. other errors. The first `ClientError` always terminates the method.

**Hallucination type:** **Assumed feature** — the AI inferred that a production S3 client would naturally have retry logic, because retry-on-timeout is a common best practice. But the actual code doesn't implement it.

**Why it's instructive:** This is the most dangerous kind of hallucination. It tests a behavior that *should* exist (retries are a good practice), which makes it easy to assume the test is correct. If this test passed, you might believe you have retry coverage when you don't.

---

### Test 7: `test_fetch_cache_raises_on_invalid_json`

**What it asserts:** `fetch_cache` catches `JSONDecodeError` and raises `S3ClientError` when the downloaded file contains invalid JSON.

**Why it's hallucinated:** The `except` block in `fetch_cache` only catches `ClientError` (from boto3). If `json.loads()` fails on invalid JSON, it raises `json.JSONDecodeError`, which is **not caught** — it propagates as an unhandled exception, not as an `S3ClientError`.

**Hallucination type:** **Assumed error handling** — the AI assumed that since the method processes JSON, it would handle JSON parse errors. But the code only catches AWS client errors, not data format errors.

**Why it's instructive:** This reveals an actual gap in the source code's error handling. The test asserts reasonable behavior that the code *doesn't* implement. This is a great discussion point: should we fix the code or accept the test is wrong? (Answer: the test is wrong as-written because it doesn't match the actual code — but it highlights a real improvement opportunity.)

---

### Test 9: `test_set_cache_compresses_large_payloads`

**What it asserts:** `set_cache` automatically gzip-compresses payloads larger than 1MB before uploading.

**Why it's hallucinated:** The `set_cache` method does `json.dumps(state).encode()` and uploads the raw bytes directly. There is **no size check, no compression logic, and no gzip import** anywhere in the file. Every payload is uploaded as plain JSON regardless of size.

**Hallucination type:** **Invented feature** — the AI fabricated an entire capability. Gzip compression for large S3 uploads is a real-world optimization, but it doesn't exist in this code at all. The test even imports `gzip` to validate decompression — a strong signal that you should check if the source code also imports `gzip` (it doesn't).

**Why it's instructive:** This is the easiest hallucination to catch if you check imports. The source file imports `boto3`, `json`, `os`, `ClientError`, `BytesIO`, and `create_log` — no `gzip`. When a test imports a module that the source doesn't use, that's a red flag.

---

## Discussion Questions

1. **Test 7 reveals a real gap.** Should `fetch_cache` catch `JSONDecodeError`? What are the tradeoffs?
2. **Test 4 tests a best practice.** How do you distinguish "the code *should* do this" from "the code *does* do this"?
3. **Test 9 imports `gzip`.** What quick checks can you run to spot hallucinations before even running the tests?
4. If all 10 tests passed, would you be confident the code works correctly? What's missing from this suite?
