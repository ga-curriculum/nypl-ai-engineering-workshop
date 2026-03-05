# NYPL — AI-Assisted Software Engineering Workshop — Q1 2026 — Pacing Guide

---

## Workshop Format

| Detail | Info |
|---|---|
| **Total Duration** | 7 hours (10:00 AM – 5:00 PM) |
| **Instruction Time** | 6 hours |
| **Lunch** | 1 hour (1:00 – 2:00 PM) |
| **Delivery Format** | Full-day, single session |
| **Cohort Size** | 25 participants |

---

## Full-Day Pacing — Minute-by-Minute

### Module 1: AI as an Engineering Partner (90 min)

| Time | Duration | Segment | Type | Notes |
|---|---|---|---|---|
| 10:00 | 20 min | Slides 1–5: Dual-tool framework + demo | Lecture + Demo | Demo: email validation with both tools |
| 10:20 | 15 min | Slides 6–8: High-context prompts + role-based prompting | Lecture | Context-specificity spectrum |
| 10:35 | 10 min | Exercise 1: Build a High-Context Prompt | Individual | Participants rewrite a vague prompt |
| 10:45 | 10 min | Exercise 2: Peer Testing Round-Robin | Pairs | Test each other's prompts in both tools |
| 10:55 | 12 min | Exercise 3: Role-Based Prompting | Individual | Security / Performance / QA roles |
| 11:07 | 8 min | Slides 9–11: Generate > Review > Refine intro | Lecture | Introduce the core loop |
| 11:15 | 5 min | Transition to Lab 1 | — | Set up lab instructions |
| 11:20 | 30 min | **Lab 1: Code Analysis** | Hands-on | 16-issue starter code, 3 tiers |
| **11:30** | — | **End of Module 1** | — | — |

> **Note:** Lab 1 timing overlaps into Module 2's slot. The agenda shows Module 1 ending at 11:30, but the lab begins at ~11:20. Manage the transition — allow 10 min for Lab 1 within Module 1, then carry the remaining 20 min into Module 2's opening.

**Adjusted flow:** Lab 1 runs 11:15–11:30 (15 min) with the understanding that participants who need more time can continue during the Module 2 lecture opening. Alternatively, extend Module 1 to 11:35 and compress Module 2 by 5 min.

### Module 2: Working with Existing Codebases (90 min)

| Time | Duration | Segment | Type | Notes |
|---|---|---|---|---|
| 11:30 | 8 min | Slides 1–4: Unfamiliar code + asking the right questions | Lecture | Transition from Lab 1 |
| 11:38 | 7 min | Slide 5: Demo — navigating the sandbox codebase | Demo | Gemini Code Assist for architecture, Copilot for functions |
| 11:45 | 5 min | Slide 6: Context windowing | Lecture | What to include, what to leave out |
| 11:50 | 8 min | Slides 7–8: Task decomposition + decomposition prompt | Lecture | Break tasks into 5–7 AI-sized chunks |
| 11:58 | 4 min | Slide 9: Context matters — same task, different context | Lecture | Before/after output quality |
| 12:02 | 12 min | Exercise 1: Decompose a Feature Request | Individual + Pairs | Human vs. AI task decomposition |
| 12:14 | 3 min | Slides 11–12: Lab preview + recap | Lecture | — |
| 12:17 | 3 min | Transition to Lab 2 | — | — |
| 12:20 | 35 min | **Lab 2: Feature Build Sprint** | Hands-on | Extend S3Client, 3 tiers |
| 12:55 | 5 min | Lab 2 Debrief | Discussion | Introduce Edge Case Hunter persona |
| **1:00** | — | **End of Module 2** | — | — |

### Lunch (60 min)

| Time | Duration | Segment |
|---|---|---|
| 1:00 | 60 min | Lunch break |
| **2:00** | — | **Resume** |

### Module 3: Testing and QA with AI (60 min)

| Time | Duration | Segment | Type | Notes |
|---|---|---|---|---|
| 2:00 | 1 min | Slides 1–2: Title + learning objectives | Lecture | — |
| 2:01 | 5 min | Slide 3: Demo — generate a test suite in 60 seconds | Demo | Copilot generates tests live |
| 2:06 | 8 min | Slides 4–5: Tests that lie + what makes a good test | Lecture | Tautological assertions, hallucinated behavior, over-mocking |
| 2:14 | 4 min | Slide 6: Introducing the Test Coverage Analyst persona | Lecture | — |
| 2:18 | 7 min | Slide 7: Demo — finding hallucinated assertions | Demo | Walk through 5 tests, tests 4 & 5 hallucinated |
| 2:25 | 3 min | Slide 8: Generate > Review > Refine for testing | Lecture | Copilot generates, Gemini Code Assist reviews |
| 2:28 | 2 min | Slides 9–10: Lab preview + recap | Lecture | — |
| 2:30 | 30 min | **Lab 3: AI Test Suite** | Hands-on | 10 tests, 3 hallucinated — run and discover failures |
| **3:00** | — | **End of Module 3** | — | — |

### Module 4: Transparency and Governance (30 min)

| Time | Duration | Segment | Type | Notes |
|---|---|---|---|---|
| 3:00 | 10 min | Slides 1–5: Disclosure spectrum + practice | Lecture | When and how to disclose AI assistance |
| 3:10 | 7 min | Slides 6–8: IP, governance, QA framework as governance | Lecture | 5 essentials for an org AI policy |
| 3:17 | 5 min | Slides 9–10: NYPL's AI Principles + Working Guidelines | Lecture | CONFIDENTIAL content — present, don't distribute |
| 3:22 | 3 min | Slide 11: Quick poll (interactive) | Interactive | Show of hands — team AI policies |
| 3:25 | 2 min | Transition to Lab 4 | — | — |
| 3:27 | 10 min | **Lab 4: Code Review Tagging** | Discussion + Hands-on | 5 code samples — tag as AI/human/assisted |
| **3:30** | — | **End of Module 4** | — | Adjusted to ~3:37 if NYPL guest speaker is included |

> **If NYPL guest speaker is confirmed (10–15 min):** Insert after Slides 9–10 and before the poll. Compress slides to compensate, or allow Module 4 to run to ~3:45 and shorten capstone by 10 min.

### Capstone Challenge (45 min)

| Time | Duration | Segment | Type | Notes |
|---|---|---|---|---|
| 3:30 | 2 min | Capstone brief and rules | Lecture | Distribute challenge-brief.md |
| 3:32 | 5 min | Phase 1: Decompose | Individual | Use Gemini Code Assist to break down the feature |
| 3:37 | 20 min | Phase 2: Implement | Individual | Use Copilot to write the code |
| 3:57 | 10 min | Phase 3: Test | Individual | Generate and review tests with AI |
| 4:07 | 8 min | Phase 4: Review | Individual | Apply Security Auditor + Edge Case Hunter |
| **4:15** | — | **End of Capstone Sprint** | — | — |

### Capstone Debrief + Wrap-up + Q&A (45 min)

| Time | Duration | Segment | Type | Notes |
|---|---|---|---|---|
| 4:15 | 20 min | Capstone debrief | Discussion | Volunteers share approaches and findings |
| 4:35 | 15 min | Workshop recap + key takeaways | Lecture | Generate > Review > Refine, dual-tool framework |
| 4:50 | 10 min | Open Q&A | Discussion | — |
| **5:00** | — | **End of Workshop** | — | — |

---

## Time Summary

| Block | Instruction | Lab/Exercise | Total |
|---|---|---|---|
| Module 1 | 60 min | 30 min (Lab 1) | 90 min |
| Module 2 | 55 min | 35 min (Lab 2) | 90 min |
| Lunch | — | — | 60 min |
| Module 3 | 30 min | 30 min (Lab 3) | 60 min |
| Module 4 | 20 min | 10 min (Lab 4) | 30 min |
| Capstone | 2 min | 43 min (sprint) | 45 min |
| Wrap-up | 45 min | — | 45 min |
| **Total** | **212 min** | **148 min** | **420 min (7 hrs)** |

**Instruction-to-practice ratio:** ~59% instruction / 41% hands-on

---

*General Assembly — All rights reserved. For educational use only.*
