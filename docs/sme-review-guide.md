# SME Review Guide — NYPL AI-Assisted Software Engineering Workshop

**Review requested:** March 1, 2026
**Delivery dates:** March 18 (Cohort 1) | March 24 (Cohort 2)
**Audience:** 25 software engineers per cohort, 2-25 years experience
**Tools:** Google Gemini Code Assist + GitHub Copilot (dual-tool framework)
**Language:** Python
**Sandbox codebase:** [NYPL-GA-Training/python-utils](https://github.com/NYPL-GA-Training/python-utils)

---

## How to Review This Repo

### 1. Set Up (15 min)

```bash
# Clone the workshop repo
git clone https://git.generalassemb.ly/modular-courses/nypl-ai-engineering-workshop.git
cd nypl-ai-engineering-workshop

# Clone the sandbox codebase (separate repo, alongside the workshop repo)
cd ..
git clone https://github.com/NYPL-GA-Training/python-utils.git
cd python-utils

# Set up and verify
python3 -m venv venv
source venv/bin/activate
pip install '.[development]'
python -m pytest           # Expect 103 tests to pass
```

No AWS credentials needed — all tests use mocks.

### 2. Understand the Structure

The workshop repo contains curriculum and instructions. The python-utils repo is the codebase participants work with during labs.

```
nypl-ai-engineering-workshop/       ← This repo (curriculum)
├── docs/                           ← Facilitator guide, setup, handouts
├── modules/                        ← 4 modules (slides + exercises)
│   ├── module-1-ai-engineering-partner/
│   ├── module-2-existing-codebase/
│   ├── module-3-testing-qa/
│   └── module-4-transparency-governance/
├── labs/                           ← 4 hands-on labs
│   ├── lab-1-code-analysis/
│   ├── lab-2-feature-build-sprint/ ← Targets s3_client.py
│   ├── lab-3-ai-test-suite/        ← Hallucinated test exercise
│   └── lab-4-code-review-tagging/
├── capstone/                       ← KMS encryption challenge
├── qa-framework/                   ← 6 QA personas + templates
├── sandbox/                        ← Clone instructions for python-utils
└── brand/                          ← GA compliance checklist

python-utils/                       ← NYPL fork (sandbox codebase)
├── src/nypl_py_utils/
│   ├── classes/
│   │   ├── s3_client.py            ← Labs 2 & 3 target
│   │   ├── kms_client.py           ← Capstone target
│   │   ├── secrets_manager_client.py
│   │   └── ...                     (10+ AWS client wrappers)
│   └── functions/
└── tests/                          (one test file per module)
```

### 3. What to Review

The review is organized by priority. Start with the items participants will touch directly, then work outward to facilitator materials.

---

## Priority 1: Lab Content (participants touch this directly)

### Lab 2: Feature Build Sprint (35 min)

**Files to review:**
- `labs/lab-2-feature-build-sprint/starter/feature-spec.md` — Feature spec participants follow
- `labs/lab-2-feature-build-sprint/solution/s3_client_extended.py` — Reference implementation
- `labs/lab-2-feature-build-sprint/review/review-checklist.md` — Edge Case Hunter persona checklist
- `python-utils/src/nypl_py_utils/classes/s3_client.py` — The source file participants modify

**What participants do:** Extend `S3Client` with new methods using Gemini Code Assist for planning and Copilot for implementation.

**Tiers:**
| Tier | Task |
|---|---|
| Base | Add `list_objects(prefix=None)` — list S3 bucket keys |
| Intermediate | Add `fetch_csv()` — download CSV, return list of dicts |
| Stretch | Add `delete_cache()` + make `resource` optional in constructor |

**Review questions:**
- [ ] Is the feature spec clear enough for a 2-5 year engineer to follow without facilitator help?
- [ ] Does the reference solution follow the existing code patterns in `s3_client.py`? (logging, error handling, `S3ClientError`)
- [ ] Are the tiers well-calibrated? Base should be achievable in 15-20 min; stretch should challenge a senior engineer for the full 35 min.
- [ ] Does the spec give enough hints without giving away the answer? (e.g., mentioning `list_objects_v2` API, `csv.DictReader`)

---

### Lab 3: AI Test Suite — Hallucinated Test Exercise (30 min)

**Files to review:**
- `labs/lab-3-ai-test-suite/starter/test_s3_client_review.py` — 10 "AI-generated" tests (3 hallucinated)
- `labs/lab-3-ai-test-suite/solution/hallucination-answers.md` — Answer key
- `python-utils/src/nypl_py_utils/classes/s3_client.py` — The source the tests are written against
- `python-utils/tests/test_s3_client.py` — The existing tests (only 2)

**What participants do:** Copy the test file into python-utils, run it, identify which 3 tests fail and explain *why* those tests assert behavior that doesn't exist.

**The 3 hallucinations:**
| Test | Hallucination | Type |
|---|---|---|
| Test 4 | Assumes retry logic on timeout | Assumed feature (code has no retry loop) |
| Test 7 | Assumes `json.JSONDecodeError` is caught as `S3ClientError` | Assumed error handling (only `ClientError` is caught) |
| Test 9 | Assumes gzip compression for large payloads | Invented feature (no gzip anywhere in the code) |

**Verification:** Run the tests yourself to confirm the pass/fail pattern:
```bash
cd python-utils
cp ../nypl-ai-engineering-workshop/labs/lab-3-ai-test-suite/starter/test_s3_client_review.py tests/
python -m pytest tests/test_s3_client_review.py -v
```
Expected: `...F..F.F.` — Tests 1,2,3,5,6,8,10 pass; Tests 4,7,9 fail.

**Review questions:**
- [ ] Do the 7 valid tests actually test real behavior? (They should all pass against the unmodified source.)
- [ ] Are the 3 hallucinations plausible enough that a participant might initially think they're correct?
- [ ] Is Test 7 (JSON error handling) a good discussion point? It reveals a real gap — should the code catch `JSONDecodeError`?
- [ ] Does the answer key explain each hallucination type clearly enough for self-study?
- [ ] Is it clear that this exercise targets the *original* `s3_client.py`, not the Lab 2 extensions?

---

### Capstone: KMS Encryption & Secret Rotation (45 min)

**Files to review:**
- `capstone/starter/challenge-brief.md` — Full challenge specification
- `capstone/review/review-checklist.md` — Security Auditor + Edge Case Hunter
- `capstone/rubric.md` — 100-point scoring rubric
- `python-utils/src/nypl_py_utils/classes/kms_client.py` — The source file participants modify
- `python-utils/tests/test_kms_client.py` — Existing tests (2 tests)
- `python-utils/src/nypl_py_utils/classes/secrets_manager_client.py` — Used in stretch tier

**What participants do:** Add `encrypt(plaintext, key_id)` to `KmsClient`, write tests, apply Security Auditor + Edge Case Hunter personas.

**Tiers:**
| Tier | Task |
|---|---|
| Base | Add `encrypt()` with base64 encoding and error handling |
| Intermediate | Add input validation + 5 tests + 2 QA persona reviews |
| Stretch | Create `rotate_secret()` integrating KmsClient + SecretsManagerClient |

**Review questions:**
- [ ] Is the challenge brief appropriate for a 45-minute timed sprint?
- [ ] Does the Security Auditor persona fit naturally? (Encryption code should trigger security thinking.)
- [ ] Is the stretch tier (cross-client integration) too ambitious for 45 minutes?
- [ ] Does the rubric scoring align with what's actually achievable per tier?
- [ ] Are there any security concerns with the hints provided? (e.g., do we give away too much about the KMS API?)

---

## Priority 2: Module Content (slides + exercises)

### Module Slides

Each module has slides in `modules/<module>/slides/slide-content.md`. These are markdown-format slide decks.

| Module | Duration | Slides File | Key Exercise Files |
|---|---|---|---|
| Module 1: AI Engineering Partner | 90 min | `module-1-ai-engineering-partner/slides/slide-content.md` | 3 exercises + Lab 1 |
| Module 2: Existing Codebases | 90 min | `module-2-existing-codebase/slides/slide-content.md` | 1 exercise + Lab 2 |
| Module 3: Testing and QA | 60 min | `module-3-testing-qa/slides/slide-content.md` | Lab 3 (no separate exercise) |
| Module 4: Transparency and Governance | 30 min | `module-4-transparency-governance/slides/slide-content.md` | 2 exercises + Lab 4 |

**Review questions for all modules:**
- [ ] Is the dual-tool framing (Gemini Code Assist = depth, Copilot = velocity) accurate and non-partisan?
- [ ] Are the demo scripts in the facilitator guide (`docs/facilitator-guide.md`) specific enough to follow cold?
- [ ] Do the exercises scale across experience levels (2-25 years)?
- [ ] Is "Gemini Code Assist" used consistently (never just "Gemini")?

---

## Priority 3: QA Framework

**Directory:** `qa-framework/`

The QA framework is the workshop's pedagogical differentiator. Six personas, each with a prompt template, evaluation checklist, and common catches:

| Persona | Used In |
|---|---|
| Security Auditor | Capstone (primary) |
| Edge Case Hunter | Lab 2, Capstone (secondary) |
| Test Coverage Analyst | Lab 3 |
| Code Readability Reviewer | General |
| Performance Engineer | General |
| Junior Dev Reviewer | General |

**Review questions:**
- [ ] Are the persona prompt templates specific enough to produce useful AI output?
- [ ] Do the "common catches" lists match what you'd actually find in NYPL's Python codebase?
- [ ] Is the example review session (`qa-framework/examples/example-review-session.md`) realistic?

---

## Priority 4: Facilitator Materials

| File | Purpose |
|---|---|
| `docs/facilitator-guide.md` | Full facilitation guide with timing, demo scripts, answer keys, contingencies |
| `docs/environment-setup.md` | Pre-workshop setup instructions for participants |
| `docs/participant-handout.md` | Day-of reference card |
| `docs/build-tracker.md` | Content completion status (all items now Done) |

**Review questions:**
- [ ] Are the timing breakdowns in the facilitator guide realistic? (Has the reviewer facilitated similar workshops?)
- [ ] Are the contingency plans (WiFi failure, Copilot issues, Gemini Code Assist issues) practical?
- [ ] Does the environment setup guide work on a clean machine? (Test it.)

---

## Known Issues for SME Attention

### ~~1. Root README.md Has Stale Setup Instructions~~ — FIXED
Updated to clone python-utils with `pip install '.[development]'`.

### ~~2. Readiness Review Document is Outdated~~ — FIXED
Updated March 1 to reflect all resolved blockers. Readiness score now 95%.

### ~~3. Participant Handout References Stale Paths~~ — FIXED
Updated to show two-repo structure (workshop + python-utils).

### ~~4. Module 3 Has No Exercises Directory Content~~ — FIXED
Added `exercises/README.md` explaining that Lab 3 serves as the exercise for this module.

### ~~5. Schedule Confirmation~~ — RESOLVED
The schedule is 10 AM – 5 PM (6 hours instruction + 1 hour lunch). The capstone is included in the agenda at 3:30–4:15 PM with debrief and wrap-up from 4:15–5:00 PM.

---

## How to Provide Feedback

1. **Create a feature branch** from `main` (branch protection requires PR review)
2. **Open a PR** with specific feedback — tag the curriculum developer
3. For quick notes, **open an issue** on the repo

If you prefer to provide feedback in a document, organize it by the priority sections above (Lab content first, then modules, then framework, then facilitator materials).

---

## Quick Verification Checklist

Run these to confirm everything works end-to-end:

```bash
# 1. python-utils installs and tests pass
cd python-utils && source venv/bin/activate && python -m pytest
# Expect: 103 passed

# 2. Hallucinated test file has correct pass/fail pattern
cp ../nypl-ai-engineering-workshop/labs/lab-3-ai-test-suite/starter/test_s3_client_review.py tests/
python -m pytest tests/test_s3_client_review.py -v
# Expect: 7 passed, 3 failed (Tests 4, 7, 9)

# 3. Lab 2 solution doesn't break existing tests
cp ../nypl-ai-engineering-workshop/labs/lab-2-feature-build-sprint/solution/s3_client_extended.py \
   src/nypl_py_utils/classes/s3_client.py
python -m pytest tests/test_s3_client.py -v
# Expect: 2 passed (existing tests still work with extended code)

# 4. Clean up
git checkout -- src/nypl_py_utils/classes/s3_client.py
rm tests/test_s3_client_review.py
```
