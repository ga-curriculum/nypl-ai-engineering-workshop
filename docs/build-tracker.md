# Build Tracker

Track what's done, in progress, and who owns what. Update this as you work.

## Status Key
- **Done** — Complete and reviewed
- **In Progress** — Actively being worked on
- **Not Started** — Queued but no work begun
- **Blocked** — Waiting on a dependency

## Infrastructure

| Item | Status | Owner | Notes |
|---|---|---|---|
| Repo scaffold and structure | Done | — | Created Feb 18 |
| README.md | Done | — | Created Feb 18 |
| CONTRIBUTING.md | Done | — | Created Feb 18 |
| Environment setup guide | Done | — | Updated Mar 1 — points to python-utils clone |
| Facilitator guide (initial) | Done | — | Updated Mar 1 — concrete file refs for all labs |
| Participant handout | Done | — | Created Feb 18 |
| Branch protection on main | Done | — | Require 1 PR review, dismiss stale reviews, admins can bypass |

## QA Framework

| Item | Status | Owner | Notes |
|---|---|---|---|
| Framework README | Done | — | Created Feb 18 |
| Security Auditor persona | Done | — | Created Feb 18 |
| Edge Case Hunter persona | Done | — | Created Feb 18 |
| Code Readability Reviewer persona | Done | — | Created Feb 18 |
| Performance Engineer persona | Done | — | Created Feb 18 |
| Junior Dev Reviewer persona | Done | — | Created Feb 18 |
| Test Coverage Analyst persona | Done | — | Created Feb 18 |
| Review templates | Done | — | Created Feb 18 |
| Example review session | Done | — | Created Feb 18 |

## Sandbox (Python Codebase)

| Item | Status | Owner | Notes |
|---|---|---|---|
| python-utils fork available | Done | — | `NYPL-GA-Training/python-utils` on GitHub |
| Sandbox README with clone instructions | Done | — | Updated Mar 1 — replaces scaffold |
| Setup verified (`pip install '.[development]'`) | Done | — | 103 tests pass on clean clone |

## Modules

| Module | Status | Owner | Notes |
|---|---|---|---|
| Module 1: AI Engineering Partner | Done | — | Slides, exercises, and answer keys complete |
| Module 2: Existing Codebases | Done | — | Slides, exercise, and lab complete — uses `s3_client.py` |
| Module 3: Testing and QA | Done | — | Slides and lab complete — hallucinated test exercise ready |
| Module 4: Transparency and Governance | Done | — | Slides, exercises, and answer keys complete |

## Labs

| Lab | Status | Owner | Notes |
|---|---|---|---|
| Lab 1: Code Analysis | Done | — | Starter code, solution, and review checklist complete |
| Lab 2: Feature Build Sprint | Done | — | Feature spec (S3Client extensions), solution, review checklist |
| Lab 3: AI Test Suite | Done | — | 10-test hallucination exercise (3 hallucinated), answer key, review checklist |
| Lab 4: Code Review Tagging | Done | — | Starter code, solution, and review checklist complete |

## Capstone

| Item | Status | Owner | Notes |
|---|---|---|---|
| Challenge brief | Done | — | KMS encrypt + secret rotation, 3 tiers |
| Review checklist | Done | — | Security Auditor (primary) + Edge Case Hunter (secondary) |
| Rubric | Done | — | Tier-specific scoring, concrete KMS examples, facilitator notes |

## Blockers

| Blocker | Impact | Owner | Target Resolution |
|---|---|---|---|
| ~~Confirm Gemini Code Assist access for 25 participants per cohort~~ | All Gemini Code Assist exercises | NYPL (Mike) | Confirmed — licenses by 3/1 |
| ~~Confirm Copilot licenses for 25 participants per cohort~~ | All Copilot exercises | NYPL (Mike) | Confirmed — licenses by 3/1 |
| ~~Sandbox codebase not yet built~~ | Labs 2, 3, capstone | — | Resolved — using NYPL-GA-Training/python-utils fork |
