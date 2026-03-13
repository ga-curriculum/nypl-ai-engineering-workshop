# Capstone Challenge

## Overview

| Detail | Info |
|---|---|
| **Duration** | 45 minutes |
| **Position** | 3:30–4:15 PM (debrief + wrap-up 4:15–5:00 PM) |
| **Tools** | Google Gemini Code Assist + GitHub Copilot |
| **QA Personas** | Security Auditor (primary) + Edge Case Hunter (secondary) |
| **Target File** | `python-utils/src/nypl_py_utils/classes/kms_client.py` |

## The Challenge

Add encryption capabilities to the `KmsClient` class and (stretch tier) build a secret rotation function that integrates `KmsClient` with `SecretsManagerClient`.

This is a timed feature sprint that brings together everything from the workshop:
- Dual-tool workflow (Gemini Code Assist + Copilot)
- Task decomposition
- AI-assisted testing
- QA Refinement Framework (Generate > Review > Refine)

## Challenge Brief

See [`starter/challenge-brief.md`](starter/challenge-brief.md) for the full specification.

### Quick Summary

| Phase | Time | Activity |
|---|---|---|
| **Decompose** | 5 min | Use Gemini Code Assist to break down the feature |
| **Implement** | 20 min | Use Copilot to write the code |
| **Test** | 10 min | Generate and review tests with AI |
| **Review** | 10 min | Apply Security Auditor + Edge Case Hunter personas |

### Tiers

| Tier | Deliverable |
|---|---|
| **Base** | Add `encrypt(plaintext, key_id)` to `KmsClient` |
| **Intermediate** | Add input validation + 5 tests + 2 QA persona reviews |
| **Stretch** | Create `rotate_secret()` integrating `KmsClient` + `SecretsManagerClient` |

**Facilitator note:** The stretch tier is intentionally ambitious for a 45-minute sprint. Participants do not need to finish the full stretch scope to succeed in the capstone.

## Evaluation Rubric

See [rubric.md](rubric.md) for detailed scoring criteria.

## Tiered Expectations

| Tier | Minimum Deliverable |
|---|---|
| Base | Working `encrypt` method + 3 tests + 1 persona review |
| Intermediate | Working `encrypt` with validation + 5 tests + 2 persona reviews |
| Stretch | Working `encrypt` + `rotate_secret` function + comprehensive test suite + all personas + written reflection |

## Codebase

This challenge uses NYPL's **python-utils** library. See [`sandbox/README.md`](../sandbox/README.md) for clone instructions and setup.

**Key files:**
- Primary target: `python-utils/src/nypl_py_utils/classes/kms_client.py`
- Existing tests: `python-utils/tests/test_kms_client.py` (2 tests)
- Stretch reference: `python-utils/src/nypl_py_utils/classes/secrets_manager_client.py`

## Starter Materials

See [`starter/challenge-brief.md`](starter/challenge-brief.md) for the full challenge specification with implementation details and hints.

## Review Criteria

See [`review/review-checklist.md`](review/review-checklist.md) for the Security Auditor + Edge Case Hunter evaluation checklist.
