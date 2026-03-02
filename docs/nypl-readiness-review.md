# NYPL Readiness Review — AI-Assisted Software Engineering Workshop

**Initial Review Date:** February 26, 2026
**Updated:** March 1, 2026
**Reviewer Perspective:** NYPL Engineering Lead
**Delivery Dates:** March 18 (Cohort 1, GA Campus Flatiron) | March 24 (Cohort 2, NYPL Trustee's Room)
**Audience:** 25 software engineers per cohort, 2-25 years experience

---

## Executive Summary

**Updated March 1:** All critical blockers from the initial review are now **resolved**. The `NYPL-GA-Training/python-utils` fork is available, and all lab content (Labs 2, 3, capstone) has been built against it. The workshop is content-complete and ready for dry run.

### Overall Readiness: 95%

| Area | Score | Status |
|---|---|---|
| Infrastructure & Documentation | 10/10 | Ready |
| QA Framework | 10/10 | Ready — workshop differentiator |
| Module Slides & Exercises | 8/10 | Ready (all 4 modules complete) |
| Lab Content | 10/10 | All 4 labs complete with starters, solutions, and review checklists |
| Sandbox Codebase | 10/10 | ~~Critical blocker~~ **Resolved** — using NYPL-GA-Training/python-utils |
| Capstone | 9/10 | Challenge brief, review checklist, and rubric complete |
| Facilitator Readiness | 9/10 | Guide updated with concrete file references and demo scripts |

---

## What's Working Well

### 1. QA Framework is a Differentiator
The six-persona QA framework (Security Auditor, Edge Case Hunter, Code Readability Reviewer, Performance Engineer, Junior Dev Reviewer, Test Coverage Analyst) is the workshop's strongest asset. Each persona has a prompt template, evaluation checklist, common catches, and usage guidance. This framework elevates the workshop from "how to use AI tools" to "how to use AI tools *responsibly*." It maps directly to NYPL's engineering values.

### 2. Dual-Tool Narrative is Consistent and Non-Partisan
Every module correctly frames Gemini Code Assist and Copilot as complementary:
- **Gemini Code Assist:** depth, 1M token context, architectural analysis, multi-agent planning
- **Copilot:** velocity, inline completion, GitHub integration, multi-model flexibility
- **Recurring metaphor (Module 2):** "Gemini Code Assist gives you the map. Copilot gives you turn-by-turn directions."

No module pitches one tool as "better." This is diplomatically smart and educationally sound.

### 3. Tool Naming is Clean
Zero instances of standalone "Gemini" across all files. Always "Gemini Code Assist." No references to GPT, ChatGPT, OpenAI, or LangChain. The `ga-compliance-checklist.md` enforces this explicitly.

### 4. Generate > Review > Refine Loop Anchors Everything
Introduced in Module 1 (Slide 10), reinforced in Module 2 (task decomposition), applied to testing in Module 3 (Slide 8 with ASCII diagram), and framed as governance in Module 4. By the capstone, participants should have internalized this loop.

### 5. Labs 1 and 4 are Production-Ready
- **Lab 1 (Code Analysis):** 107-line starter file with 16 intentional issues, 234-line solution, detailed answer key organized by category. Strong teaching material.
- **Lab 4 (Code Review Tagging):** 298-line code samples file with 5 distinct samples (3 AI-generated, 1 human-written, 1 AI-assisted), clear answer key with signal analysis.

### 6. Facilitator Guide is Comprehensive
Timing breakdowns for all 4 modules, demo scripts, exercise answer keys, contingency plans for WiFi/tool failures, and post-workshop tasks. The optional NYPL guest segment slot (Module 4) is well-positioned.

---

## Resolved Issues (as of March 1)

### ~~BLOCKER: Sandbox Codebase Does Not Exist~~ — RESOLVED

**Resolution:** The `NYPL-GA-Training/python-utils` fork is available on GitHub. Participants clone it as a separate repo and install with `pip install '.[development]'`. All 103 tests pass. No AWS credentials needed (all tests use mocks).

The `sandbox/` directory now contains clone instructions pointing to the fork. The old scaffold files (`src/`, `tasks/`, `requirements.txt`) have been removed.

### ~~Gap 1: Lab 2 Has No Feature Specification~~ — RESOLVED

**Resolution:** `labs/lab-2-feature-build-sprint/starter/feature-spec.md` contains a 3-tier feature spec for extending `S3Client` with `list_objects`, `fetch_csv`, and `delete_cache`. Reference solution in `solution/s3_client_extended.py`.

### ~~Gap 2: Lab 3 Hallucinated Test File Missing~~ — RESOLVED

**Resolution:** `labs/lab-3-ai-test-suite/starter/test_s3_client_review.py` contains 10 tests with 3 hallucinations (Tests 4, 7, 9). Verified: 7 pass, 3 fail against the actual source. Answer key in `solution/hallucination-answers.md`.

### ~~Gap 3: Capstone Challenge Brief Not Written~~ — RESOLVED

**Resolution:** `capstone/starter/challenge-brief.md` contains a KMS encryption + secret rotation challenge with 3 tiers. Review checklist (`review/review-checklist.md`) uses Security Auditor + Edge Case Hunter. Rubric updated with concrete KMS-specific scoring criteria.

---

## Remaining Gaps

### Gap 4: Module 2 Slides Lack Concrete Code Examples

Module 2 is the most abstract module. While Modules 1 and 3 have concrete Python code in slides, Module 2 relies on descriptive text and tables. For less experienced participants (2-5 years), this may feel disconnected from practice.

**Action:** Add a small Python function to Slide 9 ("Context Matters") showing before/after output quality. Can be done with generic code.

### Gap 5: Missing Answer Keys for Subjective Exercises

| Exercise | Answer Key? | Risk |
|---|---|---|
| Module 1, Exercise 1 (High-Context Prompt) | No | Facilitators must evaluate prompt quality subjectively |
| Module 1, Exercise 2 (Peer Testing) | No | Social exercise — no rubric needed (low risk) |
| Module 2, Exercise 1 (Task Decomposition) | Yes | Good coverage |
| Module 4, Exercise 1 (Disclosure Practice) | No | Open-ended scenarios with no model answers |
| Module 4, Exercise 2 (Policy Draft) | No | Group activity — no single answer (medium risk) |

**Action:** Create a brief facilitator rubric for Module 1 Exercise 1 (what makes a "good" high-context prompt — 3-4 criteria). For Module 4, add sample discussion points rather than a strict answer key.

---

## Minor Issues

### ~~1. Path Error in Environment Setup~~ — FIXED
`docs/environment-setup.md` now points to python-utils clone with `pip install '.[development]'` and `python -m pytest`.

### 2. Schedule Duration Uncertainty
The facilitator guide notes: "If confirmed as 6 hours of instruction, the additional time can expand Module 4, add a capstone challenge, or provide longer lab sessions." This has not been resolved. The current schedule assumes 5 hours.

**Action:** Confirm with NYPL whether the schedule is 5 or 6 hours of instruction. If 6, allocate the extra hour to either an expanded capstone (recommended) or longer lab sessions.

### 3. Survey Link TBD
The facilitator guide references a post-workshop survey but no link exists. Needs to be designed and tested before March 18.

### 4. Timeline Document is Stale
`docs/timeline.md` assumes February 18 as the start date. Several Week 1 items marked "Not Started" are now either done or blocked. Should be updated to reflect reality.

### 5. Module 3 Exercises Directory is Empty
The `modules/module-3-testing-qa/exercises/` directory contains only `.gitkeep`. This is intentional (testing practice is embedded in Lab 3), but a facilitator unfamiliar with the design might think content is missing. Consider adding a brief `README.md` noting that Lab 3 serves as the exercise.

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| ~~Sandbox fork not available by March 10~~ | ~~Medium~~ | ~~Critical~~ | ~~Resolved — fork available, all content built~~ |
| Gemini Code Assist extension issues on participant machines | Medium | High — demos and exercises impacted | Pre-test on 3+ machines; contingency in facilitator guide (pair up, browser fallback) |
| Copilot license activation delays | Low | Medium — some exercises impacted | Licenses confirmed by 3/1; verify activation 1 week before |
| Venue WiFi can't handle 25 connections | Low | High — all cloud-based tools fail | Pre-download dependencies; USB backup; offline Copilot fallback |
| Participants finish labs early or fall behind | Medium | Low — affects pacing | Tiered difficulty absorbs both cases; facilitator circulates |
| 6-hour schedule confirmed last minute | Low | Low — capstone content is ready | Capstone brief, rubric, and review checklist are complete |

---

## Recommended Action Plan (Updated March 1)

### ~~This Week (Feb 26-28)~~ — DONE
- [x] ~~Contact Mike Benowitz / Kimi re: python-utils fork URL~~ — Fork available
- [x] ~~Fix environment-setup.md path error~~ — Updated to python-utils clone instructions
- [x] ~~Begin writing Lab 3 hallucinated test file~~ — Complete with 10 tests (3 hallucinated)

### Week of March 2-6
- [x] ~~Integrate sandbox codebase~~ — python-utils integrated, all labs point to it
- [x] ~~Write Lab 2 feature spec and solution~~ — Complete (S3Client extensions, 3 tiers)
- [x] ~~Write Lab 3 solution~~ — Complete (hallucination answer key)
- [x] ~~Write capstone challenge brief~~ — Complete (KMS encrypt + secret rotation)
- [ ] Confirm 5 vs. 6 hour schedule with NYPL
- [ ] Create facilitator rubric for Module 1 Exercise 1
- [ ] Design post-workshop survey
- [ ] Update `docs/timeline.md` to reflect current reality
- [ ] SME review (see `docs/sme-review-guide.md`)

### Week of March 9-13
- [ ] Full dry run (simulate 5-hour workshop end-to-end)
- [ ] Test fresh clone + environment setup on clean machine
- [ ] Pre-test Gemini Code Assist and Copilot extensions on 3+ machines
- [ ] Finalize participant handout and print if needed
- [ ] **GO/NO-GO decision for March 18**

### March 16-17
- [ ] Fix any issues from dry run
- [ ] Verify all licenses activated (Gemini Code Assist + Copilot for 25 participants)
- [ ] Stage USB backup with repo + dependencies

---

## Summary

**What's strong:** The pedagogical design, QA framework, dual-tool narrative, and facilitator support are all excellent. All 4 labs are production-ready with starters, solutions, and review checklists. The Generate > Review > Refine loop is a compelling throughline. Tool naming is clean.

**What was resolved:** The sandbox codebase blocker — the single critical-path dependency from the initial review — is fully resolved. Labs 2, 3, and the capstone now have concrete content built against NYPL's actual python-utils codebase.

**What remains:** Minor polish items (Module 2 slide examples, subjective exercise rubrics, schedule confirmation, survey design). None are blockers. The workshop is ready for dry run.

**Next milestone:** Full dry run during the week of March 9-13.
