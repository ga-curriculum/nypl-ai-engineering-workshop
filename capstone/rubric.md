# Capstone Evaluation Rubric

## Challenge: KMS Encryption & Secret Rotation

Target file: `python-utils/src/nypl_py_utils/classes/kms_client.py`

## Scoring Categories

### 1. Task Decomposition (20 points)

| Score | Criteria |
|---|---|
| 20 | Feature broken into clear, logical steps; each step is AI-appropriate in scope. Example: separate steps for imports, method signature, KMS API call, base64 encoding, error handling, logging. |
| 15 | Reasonable decomposition with minor gaps in step sizing |
| 10 | Decomposition attempted but steps are too large or too vague (e.g., "implement encrypt method" as a single step) |
| 5 | Minimal decomposition; jumped straight to implementation |

**What to look for:** Did they use Gemini Code Assist to decompose? Is the breakdown granular enough that each step could be a single Copilot prompt?

### 2. Implementation Quality (30 points)

| Score | Criteria |
|---|---|
| 30 | `encrypt()` works correctly; uses `b64encode`, calls `kms_client.encrypt()` with correct params, follows existing patterns (logging, error handling, `KmsClientError`). Stretch: `rotate_secret()` correctly integrates both clients. |
| 22 | `encrypt()` works; minor gaps — e.g., missing logging, inconsistent error handling style |
| 15 | `encrypt()` partially works; issues with base64 encoding, wrong KMS API params, or missing error wrapping |
| 8 | Method attempted but doesn't work or has significant issues |

**Tier-specific expectations:**

| Tier | Minimum for full marks in this category |
|---|---|
| Base | Working `encrypt(plaintext, key_id)` that returns a base64-encoded string |
| Intermediate | Above + input validation (non-empty string checks) |
| Stretch | Above + `rotate_secret()` function + `set_secret()` on SecretsManagerClient |

### 3. AI Tool Usage (20 points)

| Score | Criteria |
|---|---|
| 20 | Effective dual-tool workflow: Gemini Code Assist for planning/review (e.g., "What does the KMS encrypt API return?", "Review my error handling"), Copilot for implementation (inline completions, test generation) |
| 15 | Good use of tools but leaned heavily on one; missed opportunities for the other |
| 10 | Used tools but without clear strategy; prompts were generic (e.g., "write an encrypt function") |
| 5 | Minimal tool usage; mostly manual coding |

**What to look for:** Did they use Gemini Code Assist to understand the KMS API before coding? Did they use Copilot's inline suggestions to follow the existing pattern (matching `decrypt`'s structure)?

### 4. Testing (15 points)

| Score | Criteria |
|---|---|
| 15 | 5+ tests covering: happy path, correct KMS API params, empty plaintext, empty key_id, ClientError handling. No hallucinated assertions. Tests match actual code behavior. |
| 11 | 3-4 tests covering happy path and some edge cases; minor issues |
| 7 | Tests present but shallow (e.g., only happy path), or contain hallucinated assertions (testing behavior that doesn't exist) |
| 3 | Minimal or no tests |

**Key tests to look for:**
- Happy path: encrypts and returns base64 string
- Verifies `kms_client.encrypt` called with `KeyId` and `Plaintext` params
- Input validation: raises `KmsClientError` on empty/None inputs (intermediate+)
- Error handling: raises `KmsClientError` when KMS API returns `ClientError`
- Stretch: `rotate_secret` encrypts before storing, closes both clients

### 5. QA Review (15 points)

| Score | Criteria |
|---|---|
| 15 | Applied Security Auditor + Edge Case Hunter; identified real issues (e.g., plaintext in logs, missing input validation, partial failure in rotation); refined code based on findings |
| 11 | Applied 1 persona thoroughly; some refinement based on findings |
| 7 | Review attempted but superficial; checked boxes without meaningful analysis |
| 3 | No review step applied |

**Security Auditor red flags to catch:**
- Plaintext values logged in `self.logger` calls (data exposure)
- Error messages that include sensitive input values
- Stretch: `rotate_secret` doesn't use try/finally to ensure client cleanup

**Edge Case Hunter items to catch:**
- Unicode input to `encrypt` (emoji, CJK characters)
- Very large plaintext values
- Calling `encrypt` after `close()`

## Total: 100 points

| Grade | Score | Description |
|---|---|---|
| Exceeds Expectations | 85-100 | Ready to integrate AI tools into daily workflow |
| Meets Expectations | 65-84 | Solid foundation; needs practice to build fluency |
| Approaching | 45-64 | Understands concepts; needs more hands-on time |
| Needs Support | Below 45 | Requires additional training or 1:1 guidance |

## Tier Baseline Expectations

| Tier | Typical Score Range | Expected Deliverables |
|---|---|---|
| Base (2-5 yrs) | 45-70 | Working `encrypt` + 3 tests + 1 persona |
| Intermediate (5-15 yrs) | 65-85 | `encrypt` with validation + 5 tests + 2 personas |
| Stretch (15-25 yrs) | 80-100 | Full implementation + `rotate_secret` + comprehensive tests + all personas |

## Facilitator Notes

- This is formative, not summative — use scores to guide debrief discussion, not to grade participants
- The most valuable debrief question: "What did the Security Auditor persona catch that you would have missed?"
- If time is short, focus evaluation on categories 2 (Implementation) and 5 (QA Review) — these demonstrate the core workshop skills
