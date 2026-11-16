# NYPL — AI-Assisted Software Engineering Workshop — Q1 2026 — Instructor Guide

---

## 1. Program Overview

### Course Description

A 6-hour in-person workshop teaching software engineers how to integrate AI tools into professional development workflows. Participants learn to use **Google Gemini Code Assist** and **GitHub Copilot** as complementary engineering tools through hands-on labs, a structured QA refinement framework, and a timed capstone challenge — all built on NYPL's own Python codebase.

### Key Features

- **Dual-tool framework:** Gemini Code Assist (depth, 1M token context, architectural analysis) + GitHub Copilot (velocity, inline completion, GitHub integration)
- **QA Refinement Framework:** Six QA personas that teach engineers to never ship AI output without structured review
- **Generate > Review > Refine loop:** Core methodology applied in every lab and the capstone
- **Real codebase:** All labs use NYPL's `python-utils` library — not toy examples
- **Tiered difficulty:** Every lab has Base (2–5 yr), Intermediate (5–15 yr), and Stretch (15–25 yr) tiers
- **NYPL AI Guidelines integration:** Module 4 incorporates NYPL's official AI Principles & Working Staff Guidelines

### Program Outline

| Block | Topic | Duration | Type |
|---|---|---|---|
| Module 1 | AI as an Engineering Partner | 90 min | Lecture + Lab 1 |
| Module 2 | Working with Existing Codebases | 90 min | Lecture + Lab 2 |
| Lunch | — | 60 min | — |
| Module 3 | Testing and QA with AI | 60 min | Lecture + Lab 3 |
| Module 4 | Transparency and Governance | 30 min | Lecture + Lab 4 |
| Capstone | Encryption Feature Sprint | 45 min | Hands-on sprint |
| Wrap-up | Capstone Debrief + Q&A | 45 min | Plenary |

### Schedule

- **Duration:** 10:00 AM – 5:00 PM ET (6 hours instruction + 1 hour lunch)
- **Delivery Dates:** March 18, 2026 (Cohort 1) | March 24, 2026 (Cohort 2)
- **Cohort Size:** 25 software engineers per session
- **Format:** In-person, devices required

### Audience

- 25 software engineers per cohort (SE, QA, DevOps roles)
- Experience range: 2 to 25 years
- All participants have Python experience
- All participants have GitHub accounts

### Language

- Programming language: **Python**
- Instruction language: **English**

### Delivery Strategy

- In-person with participant devices (laptops)
- VS Code as the primary IDE
- Two repos: workshop curriculum repo + NYPL's python-utils sandbox repo
- Facilitator circulates during labs; participants work individually but may pair up
- Tiered difficulty absorbs the experience range — no one finishes early or falls behind

---

## 2. How to Adapt the Program

### Step 1: Familiarize Yourself with All Program Resources

Review the following in order:

| Resource | Location | Purpose |
|---|---|---|
| Workshop README | `README.md` | High-level overview |
| Facilitator Guide | `docs/facilitator-guide.md` | Detailed timing, demo scripts, answer keys, contingencies |
| Participant Handout | `docs/participant-handout.md` | What participants receive day-of |
| Environment Setup | `docs/environment-setup.md` | Pre-workshop setup instructions |
| QA Framework | `qa-framework/README.md` | The 6 QA personas and review methodology |
| Module READMEs | `modules/module-*/README.md` | Learning objectives and content outlines |
| Lab READMEs | `labs/lab-*/README.md` | Lab instructions with tiered difficulty |
| Capstone | `capstone/README.md` | Final challenge specification |
| NYPL AI Guidelines | `modules/module-4-transparency-governance/slides/nypl-ai-guidelines-CONFIDENTIAL.md` | CONFIDENTIAL — for Module 4 delivery only |

### Step 2: Identify Pre-Work Requirements

Participants must complete the environment setup **before** the workshop (allow 20–30 min):

1. Clone the workshop repo from `github.com`
2. Clone `NYPL-GA-Training/python-utils` from GitHub
3. Set up Python virtual environment and install dependencies
4. Install and verify GitHub Copilot extension in VS Code
5. Install and verify Google Gemini Code Assist extension in VS Code
6. Run `python -m pytest` in python-utils to confirm 103 tests pass

Full instructions: `docs/environment-setup.md`

### Step 3: Copy and Verify Resources

```bash
# Clone the workshop repo
git clone https://github.com/ga-curriculum/nypl-ai-engineering-workshop.git

# Clone the sandbox codebase (separate repo)
git clone https://github.com/NYPL-GA-Training/python-utils.git
cd python-utils
python -m venv venv
source venv/bin/activate
pip install '.[development]'
python -m pytest   # Expect 103 tests passed
```

### Step 4: Identify Sections Needing Customization

> **Customize It!** The following areas may need adjustment per cohort:

- **Participant experience level distribution** — Adjust pacing if the cohort skews junior or senior. Do a show-of-hands at the start to gauge.
- **NYPL guest speaker** — Module 4 has an optional 10–15 min slot for NYPL leadership (Garvita or team lead) to present their internal AI guidelines. Confirm if this is happening and adjust Module 4 timing.
- **Venue-specific logistics** — Cohort 1 (GA Campus, Flatiron NYC) is hybrid-capable. Cohort 2 (NYPL Trustee's Room, Bryant Park) is NOT hybrid-capable.

### Step 5: Remote Delivery Adjustments

This workshop is designed for **in-person delivery only**. If remote delivery is required:

- All demos work via screen share
- Labs work individually (participants work on their own machines)
- Use breakout rooms for peer exercises (Module 1 Exercise 2, Module 4 Exercise 2)
- The code review tagging exercise (Lab 4) works well in chat-based discussion
- Capstone debrief can use screen sharing for volunteer presentations

### Step 6: Welcome/Kick-off Customization

- Add instructor bio and photo to opening slides
- Mention cohort-specific venue details (wifi password, restrooms, etc.)
- Reference NYPL's engineering team context if known

### Step 7: Code Repository Verification

Before each delivery, run the full verification checklist:

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
# Expect: 2 passed

# 4. Clean up
git checkout -- src/nypl_py_utils/classes/s3_client.py
rm tests/test_s3_client_review.py
```

### Step 8: Localization Considerations

- No localization required — delivery is in English, in-person in NYC
- All code examples use Python with English variable names and comments
- NYPL's AI Guidelines document is in English

### Step 9: Share Resources with Co-Instructors

Share the following with any co-instructor or TA:

1. This Instructor Guide
2. The Facilitator Guide (`docs/facilitator-guide.md`) — contains demo scripts and answer keys
3. Repo access (both workshop repo and python-utils)
4. The Pacing Guide

Discuss teaching plan and division of responsibilities (e.g., who leads which module, who circulates during labs).

### Step 10: Align with Pacing Guide

Review the Pacing Guide to confirm timing for your delivery. The current pacing is:

- **Morning block:** 3 hours (Modules 1–2, 10:00 AM – 1:00 PM)
- **Lunch:** 1 hour (1:00 – 2:00 PM)
- **Afternoon block:** 3 hours (Modules 3–4 + Capstone + Wrap-up, 2:00 – 5:00 PM)

---

## 3. Key Links and Resources

### Program Materials

| Resource | Location |
|---|---|
| Workshop Repository | `../` |
| Sandbox Codebase | `github.com/NYPL-GA-Training/python-utils` |
| Facilitator Guide | `docs/facilitator-guide.md` |
| Participant Handout | `docs/participant-handout.md` |
| Environment Setup | `docs/environment-setup.md` |
| QA Framework | `qa-framework/README.md` |
| NYPL AI Guidelines (CONFIDENTIAL) | `modules/module-4-transparency-governance/slides/nypl-ai-guidelines-CONFIDENTIAL.md` |

### Content Development Resources

- **Sourcing examples:** All code examples use NYPL's `python-utils` library
- **Creating exercises:** Labs follow starter → solution → review structure with 3 difficulty tiers
- **Inclusive content:** Tiered difficulty accommodates 2–25 years of experience; no assumptions about prior AI tool usage

### Design Resources

- Follow GA brand guidelines (see `brand/ga-compliance-checklist.md`)
- Tool naming: Always use "Google Gemini Code Assist" (never standalone "Gemini") and "GitHub Copilot"
- No references to GPT, ChatGPT, OpenAI, or LangChain in participant-facing materials

---

## 4. Program Preparation Checklist

### Getting Started (2+ weeks before delivery)

- [ ] Review all program materials (see Step 1 above)
- [ ] Clone both repos and complete environment setup on your own machine
- [ ] Run the full code verification checklist (see Step 7)
- [ ] Review the NYPL AI Guidelines (CONFIDENTIAL) for Module 4

### During Adaptation (1–2 weeks before delivery)

- [ ] Confirm participant list (25 per cohort) and experience level distribution
- [ ] Confirm GitHub Copilot licenses are activated for all participants
- [ ] Confirm Gemini Code Assist access for all participants
- [ ] Confirm NYPL guest speaker for Module 4 (optional — adjust timing if confirmed)
- [ ] Test fresh clone + setup on a clean machine
- [ ] Test Gemini Code Assist and Copilot extensions on 3+ machines
- [ ] Run full dry run (simulate 6-hour workshop end-to-end)
- [ ] Print participant handouts if applicable

### Before Delivery (day before + day of)

- [ ] Verify venue WiFi can handle 25+ simultaneous connections
- [ ] Test screen sharing / projector setup
- [ ] Prepare backup materials (USB drive with repo + dependencies for WiFi failure)
- [ ] Arrive 30 min early for setup
- [ ] Display environment-setup.md on screen as participants arrive
- [ ] Do a quick show-of-hands to gauge experience levels

### Post-Delivery

- [ ] Collect participant feedback (survey)
- [ ] Share repo access with participants for continued practice
- [ ] Send follow-up resources email within 48 hours
- [ ] Document timing adjustments for next cohort (Cohort 1 → Cohort 2)

---

## 5. Module Facilitation Notes

For detailed timing breakdowns, demo scripts, exercise answer keys, and contingency plans, see `docs/facilitator-guide.md`.

### Module 1: AI as an Engineering Partner (90 min, 10:00–11:30)

**Goal:** Participants understand the dual-tool framework and can use both tools for code generation.

**Key moments:**
- Demo (Slide 5): Same email validation task given to both tools — Gemini Code Assist shows depth, Copilot shows speed
- Exercise 1: Build a high-context prompt (rubric: specific function name, clear types, edge cases, style requirements)
- Exercise 2: Peer testing round-robin (social energy builder)
- Exercise 3: Role-based prompting with security/performance/QA roles (answer key in facilitator guide)
- Lab 1: 16-issue starter code in `inventory_manager.py` (answer key in `solution/issues-found.md`)

### Module 2: Working with Existing Codebases (90 min, 11:30–1:00)

**Goal:** Participants can navigate, understand, and extend unfamiliar code with AI.

**Key moments:**
- Demo (Slide 5): Navigate python-utils with Gemini Code Assist (architectural overview) + Copilot (function-level explanation)
- Exercise 1: Task decomposition — compare human vs. AI approaches
- Lab 2: Extend `S3Client` with `list_objects`, `fetch_csv`, `delete_cache` (3 tiers)
- Lab 2 does NOT need to be finished — Lab 3 uses the original `s3_client.py`

### Module 3: Testing and QA with AI (60 min, 2:00–3:00)

**Goal:** Participants can generate, evaluate, and refine test suites.

**Key moments:**
- Demo (Slide 7): Walk through 5 tests — first 3 good, tests 4 & 5 hallucinated. Ask: "Would you have caught these?"
- Lab 3: 10 tests, 3 hallucinated (Tests 4, 7, 9) — participants discover failures by running the tests
- This is the most memorable teaching moment — let participants discover the failures, then discuss

### Module 4: Transparency and Governance (30 min, 3:00–3:30)

**Goal:** Awareness of responsible AI use and organizational governance.

**Key moments:**
- Slides 9–10: Present NYPL's AI Principles (from CONFIDENTIAL doc — do not distribute)
- Optional NYPL guest speaker (10–15 min) — adjust timing if confirmed
- Lab 4: Tag 5 code samples as AI-generated, human-written, or AI-assisted
- Use as segue to capstone: "Now use everything you've learned"

### Capstone (45 min, 3:30–4:15) + Debrief (45 min, 4:15–5:00)

**Goal:** Integrate all skills in a timed sprint.

- KMS encryption challenge using `kms_client.py`
- Phases: Decompose (5 min) → Implement (20 min) → Test (10 min) → Review (10 min)
- Security Auditor + Edge Case Hunter personas for review
- Debrief: Volunteers share approaches, discuss where AI helped vs. struggled

---

## 6. Contingency Plans

### Copilot Not Working
- Pair participants (one types, one navigates)
- Use instructor screen share for demos
- Copilot chat in browser (github.com/copilot) as fallback

### Gemini Code Assist Extension Issues
- Sign out and sign back in
- Check for conflicting AI extensions (disable others)
- Pair participants with a neighbor
- Pre-record demo videos as backup

### WiFi Issues
- Pre-download all dependencies into the sandbox venv
- USB drive with repo + dependencies
- Copilot inline suggestions work offline

---

*General Assembly — All rights reserved. For educational use only.*
