# March 13 Readiness Update

**Author:** Arthur Bernier  
**Date:** March 13, 2026  
**Scope:** Final documentation alignment pass before March 18 delivery

---

## Purpose

This document summarizes the final readiness review performed on March 13 and explains the documentation changes that were made as a result.

The goal of this pass was not to redesign the workshop. The workshop is already structurally strong. The goal was to identify and fix documentation inconsistencies, timing mismatches, and expectation-setting gaps that could create confusion during facilitation.

---

## Overall Assessment

The workshop is in strong shape and very close to ready for delivery.

What is working well:
- The full-day flow is coherent for a one-day, 6-hour workshop.
- The labs build conceptually across the day.
- The Gemini Code Assist / GitHub Copilot split is consistent and credible.
- The tiered lab structure supports mixed experience levels.
- The capstone is appropriate as a final sprint, provided expectations are framed clearly.

What needed attention:
- A few docs contradicted each other on lab dependencies and timing.
- Module 3 slide language could cause confusion between the warm-up demo and the actual Lab 3 exercise.
- Lab 1 and the capstone needed clearer expectation-setting for facilitation.
- Lab 3 needed an explicit cleanup/reset note after the intentionally failing review test exercise.

---

## Files Updated

The following files were updated in this pass:

- `README.md`
- `modules/module-2-existing-codebase/README.md`
- `modules/module-3-testing-qa/slides/slide-content.md`
- `docs/facilitator-guide.md`
- `capstone/README.md`
- `capstone/starter/challenge-brief.md`
- `labs/lab-3-ai-test-suite/README.md`

---

## Change Summary

### 1. Clarified Lab 3 dependency wording

**File:** `README.md`

Updated the top-level lab table so Lab 3 no longer appears to depend on "Lab 2 output."

Why:
- The actual Lab 3 materials correctly use the original `s3_client.py`.
- Leaving the old wording in place could lead facilitators or participants to think Lab 2 must be completed first.

Result:
- The repo now reflects the intended flow more accurately.

### 2. Normalized Module 2 timing language

**File:** `modules/module-2-existing-codebase/README.md`

Updated the duration wording so it matches the rest of the workshop materials, which treat Lab 2 as a 35-minute lab rather than a 30-minute lab.

Why:
- One doc still used the older timing breakdown.
- Consistent timing matters for planning and facilitation.

Result:
- Module 2 timing is now aligned with the agenda and facilitator guide.

### 3. Clarified the difference between the Module 3 demo and Lab 3

**File:** `modules/module-3-testing-qa/slides/slide-content.md`

Added a note explicitly stating that the `get_active_users` slide demo is separate from the actual Lab 3 `s3_client.py` exercise. Also updated the Lab 3 preview so the base-tier description matches the real participant workflow.

Why:
- The slide deck uses a 5-test warm-up example where Tests 4 and 5 are hallucinated.
- The actual Lab 3 exercise uses a separate 10-test file where Tests 4, 7, and 9 are hallucinated.
- Without this clarification, the slide language could make the lab seem inconsistent even though the materials are correct.

Result:
- Facilitators can present the warm-up demo without creating confusion about the actual lab answer key.

### 4. Added facilitation guidance for Lab 1 and Lab 3

**File:** `docs/facilitator-guide.md`

Added three clarifications:
- Lab 1 timing note: 15 minutes is realistic for base-tier completion, while the full 30 minutes supports deeper work.
- Module 3 demo note: the `get_active_users` example is a warm-up, not the actual Lab 3 exercise.
- Lab 3 cleanup note: remove the copied review test file after the exercise so later test runs are not polluted by intentional failures.

Why:
- These are practical facilitation details that surfaced during the dry run.
- They reduce ambiguity and help avoid avoidable confusion during delivery.

Result:
- The facilitator guide now better reflects the real classroom experience.

### 5. Added capstone expectation-setting

**Files:**
- `capstone/README.md`
- `capstone/starter/challenge-brief.md`

Added a note that the stretch tier is intentionally ambitious for a 45-minute sprint and that full stretch completion is not expected.

Why:
- The capstone stretch scope is valuable, but broad for the available time.
- Participants should not feel they failed if they make strong partial progress without completing the entire stretch path.

Result:
- Capstone expectations now match the actual time available.

### 6. Added Lab 3 cleanup guidance

**File:** `labs/lab-3-ai-test-suite/README.md`

Added a cleanup section explaining that the copied review test file is intentionally designed to fail three tests and should be removed or reset before running the full `python-utils` test suite again.

Why:
- During the dry run, leaving the copied file in place caused the full test suite to appear broken even though the exercise was functioning correctly.

Result:
- The Lab 3 workflow now includes the operational detail needed to keep the sandbox clean.

---

## What Was Verified During Review

During the readiness pass, the workshop was walked end-to-end at a practical level to confirm that the labs and capstone were feasible and that the documentation matched the experience.

Key findings:
- Lab 1 is solid, but the base tier is better framed as a 15-minute path rather than assuming everyone will use the full 30 minutes the same way.
- Lab 2 is workable as written and the 35-minute framing is more accurate than 30 minutes.
- Lab 3 behaves as intended, but it benefits from a cleanup/reset note after the copied exercise file is run.
- The capstone is appropriate for the day, but the stretch tier needs explicit expectation-setting.

---

## What Was Not Included In This Push

This update was intentionally limited to curriculum and documentation changes.

Not included:
- Any rehearsal-only `python-utils` implementation changes
- Any rehearsal-only `python-utils` test additions
- Any solution code created solely to validate feasibility during review

Why:
- The participant sandbox should remain unsolved.
- The goal of this push was to improve instructional clarity, not pre-complete participant work.

---

## Bottom Line

This pass did not change the core workshop design. It tightened the documentation so that the repo better matches the actual facilitation plan and participant experience.

The workshop remains a strong one-day, 6-hour session. These changes are intended to reduce confusion, improve pacing clarity, and make delivery smoother on March 18.
