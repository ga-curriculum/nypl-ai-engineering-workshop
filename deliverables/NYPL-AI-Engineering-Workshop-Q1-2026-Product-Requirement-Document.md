# NYPL — AI-Assisted Software Engineering Workshop — Q1 2026 — Product Requirement Document

---

## Core Information for Handoff to LPD

### RACI

| Role | Name / Team | Responsibility |
|---|---|---|
| **Responsible** | Curriculum Developer | Content development, repo build, lab design |
| **Accountable** | Program Manager / LED | Program quality, timeline, client relationship |
| **Consulted** | SME Reviewer | Technical accuracy, lab calibration, code review |
| **Informed** | NYPL Engineering Lead (Mike Benowitz) | Content alignment with NYPL needs, tool access, participant coordination |

### General Notes

- This is a **custom workshop** built for NYPL's software engineering team
- All content uses NYPL's own `python-utils` codebase as the sandbox
- Dual-tool framework (Gemini Code Assist + Copilot) — non-partisan framing required
- NYPL's internal AI Guidelines (CONFIDENTIAL) are integrated into Module 4
- Two identical deliveries: March 18 (Cohort 1) and March 24 (Cohort 2)

---

## Sales & Context Information

### Timeline and Milestones

| Milestone | Date | Status |
|---|---|---|
| Stakeholder Kickoff | Week of Feb 18, 2026 | Complete |
| Content Development Start | Feb 18, 2026 | Complete |
| HLD Review | Week of Feb 24, 2026 | Complete |
| Sandbox Codebase Available | Feb 28, 2026 | Complete |
| Content Complete (Draft) | Mar 6, 2026 | Complete |
| SME Review | Week of Mar 2, 2026 | In Progress |
| Full Dry Run | Week of Mar 9, 2026 | Scheduled |
| Final Polish | Mar 16–17, 2026 | Scheduled |
| **Delivery 1 (Cohort 1)** | **Mar 18, 2026** | Scheduled |
| **Delivery 2 (Cohort 2)** | **Mar 24, 2026** | Scheduled |

---

## Problem & Learning Outcomes

### Problem Client is Trying to Solve

NYPL's engineering team (50 engineers across SE, QA, and DevOps) needs structured training on integrating AI coding tools into their professional workflows. Engineers are using AI tools ad hoc without consistent practices for prompt engineering, code review, testing, or governance. NYPL wants to establish a responsible, effective approach to AI-assisted development that aligns with their organizational AI principles.

### Learning Outcomes / Client Expectations

Participants will be able to:

1. Use Gemini Code Assist and Copilot as complementary engineering tools
2. Write effective, high-context prompts for code generation
3. Navigate and extend unfamiliar codebases using AI assistance
4. Generate and evaluate AI-produced test suites — identifying hallucinated tests
5. Apply the Generate > Review > Refine loop as a standard workflow
6. Use structured QA personas to review AI output before shipping
7. Articulate when and how to disclose AI assistance
8. Align personal AI usage with NYPL's organizational guidelines

### Customization Level

**Level 4: More than 50% net new build**

Justification:
- Custom sandbox codebase (NYPL's `python-utils` library)
- Custom labs built against NYPL's actual code
- NYPL's CONFIDENTIAL AI Guidelines integrated into Module 4
- Custom QA framework with 6 personas designed for this workshop
- Custom capstone challenge targeting NYPL's `KmsClient`
- Dual-tool framework (Gemini Code Assist + Copilot) is a custom design
- Adapted from source repo (`ai-for-se-workshop`) but substantially rebuilt

---

## Budget & Branding

### Branding

| Element | Requirement |
|---|---|
| **Primary branding** | General Assembly |
| **Co-branding** | NYPL acknowledged as client in internal materials only |
| **Tool naming** | "Google Gemini Code Assist" (never standalone "Gemini"); "GitHub Copilot" |
| **Prohibited references** | No GPT, ChatGPT, OpenAI, or LangChain in participant-facing materials |
| **Compliance** | See `brand/ga-compliance-checklist.md` |

---

## Technical Requirements

### Required Tools & Software

| Tool | Version / Notes | License Required |
|---|---|---|
| Python | 3.10+ | Free (pre-installed or participant installs) |
| VS Code | Latest stable | Free |
| Git | Latest stable | Free |
| GitHub Copilot | VS Code extension | Yes — NYPL provides licenses for 25 participants per cohort |
| Google Gemini Code Assist | VS Code extension | Yes — Google account access verified |
| pytest | Installed via `pip install '.[development]'` | Free (included in python-utils) |

### Required Accounts

| Account | Provider | Notes |
|---|---|---|
| GitHub | GitHub | Participants need NYPL org membership for Copilot license |
| Google | Google | For Gemini Code Assist extension sign-in |

### Operating Systems

- macOS or Windows (Linux supported but not tested)
- VS Code runs on all platforms

### Sandbox / VM

- No VM required — participants work on their own laptops
- Two repos cloned locally: workshop repo + python-utils
- Python virtual environment for dependency isolation
- No AWS credentials needed — all tests use mocks

---

## Delivery Information

### Schedule

| Detail | Info |
|---|---|
| **Total Hours** | 7 hours (6 instruction + 1 lunch) |
| **Hours Per Day** | 7 (single-day delivery) |
| **Schedule** | 10:00 AM – 5:00 PM ET |
| **Spread** | 1 day per cohort, 2 cohorts total |

### Delivery Format

| Detail | Info |
|---|---|
| **Format** | In-person, devices required |
| **Platform** | N/A (in-person) |
| **Cohort 1 Venue** | GA Campus, Flatiron NYC (hybrid-capable) |
| **Cohort 2 Venue** | NYPL Trustee's Room, Bryant Park (NOT hybrid-capable) |

### Learners

| Detail | Info |
|---|---|
| **Number per cohort** | 25 |
| **Total** | 50 (2 cohorts) |
| **Roles** | Software Engineer, QA Engineer, DevOps Engineer |
| **Experience range** | 2 to 25 years |
| **Prerequisites** | Python experience, GitHub account |

### Assessment Mechanism

- **Capstone challenge:** 45-min timed feature sprint with 100-point rubric
- **Tiered difficulty:** Base / Intermediate / Stretch tiers in all labs
- **QA review:** Participants apply Security Auditor + Edge Case Hunter personas to their own code
- **No formal grading** — workshop format, not course

### Success Metrics

- Participant confidence survey (pre/post)
- Capstone completion rate across tiers
- Qualitative feedback on dual-tool framework adoption intent
- Facilitator observations on engagement and pacing

---

## Resources & References

### Source Content

| Resource | Notes |
|---|---|
| `ai-for-se-workshop` source repo | Adapted — Copilot module, prompt development, advanced prompting |
| NYPL `python-utils` library | Sandbox codebase for all labs |
| NYPL AI Principles & Working Staff Guidelines | CONFIDENTIAL — integrated into Module 4 |

### Translation / Localization

- Not required — English delivery in NYC

---

*General Assembly — All rights reserved. For educational use only.*
