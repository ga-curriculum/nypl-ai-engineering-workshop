# AI-Assisted Software Engineering Workshop — NYPL

A 6-hour in-person workshop for the New York Public Library, teaching software engineers how to integrate AI tools into professional development workflows using **Google Gemini Code Assist** and **GitHub Copilot**.

## Workshop Overview

| Detail | Info |
|---|---|
| **Client** | New York Public Library (NYPL) |
| **Audience** | 25 software engineers per session (SE, QA, DevOps) — 2 to 25 years experience |
| **Duration** | 10 AM – 5 PM (6 hours instruction + 1 hour lunch), in-person with devices |
| **Delivery Dates** | March 18, 2026 (Cohort 1) and March 24, 2026 (Cohort 2) |
| **Tools** | Google Gemini Code Assist + GitHub Copilot (dual-tool framework) |
| **Language** | Python |

## Modules

| Module | Topic | Duration |
|---|---|---|
| 1 | AI as an Engineering Partner | 90 min |
| 2 | Working with Existing Codebases | 90 min |
| 3 | Testing and QA with AI | 60 min |
| 4 | Transparency and Governance | 30 min |
| Capstone | Encryption Feature Sprint | 45 min |

## Labs

| Lab | Focus | Builds On |
|---|---|---|
| 1 | Code Analysis | Module 1 |
| 2 | Feature Build Sprint | Module 2 |
| 3 | AI Test Suite | Module 3 (uses original `s3_client.py`) |
| 4 | Code Review and Tagging | Module 4 |

## QA Refinement Framework

Every lab follows the **Generate > Review > Refine** loop. AI-generated code is evaluated by QA personas (security auditor, edge-case hunter, performance engineer, etc.) before being accepted. This teaches engineers to never ship AI output without structured review.

See [qa-framework/README.md](qa-framework/README.md) for full details.

## Repository Structure

```
nypl-ai-engineering-workshop/
├── docs/                    # Facilitator guide, participant handout, setup, timeline
├── modules/                 # 4 workshop modules (slides + exercises)
├── labs/                    # 4 hands-on labs (starter, solution, review)
├── sandbox/                 # Clone instructions for python-utils (the sandbox codebase)
├── qa-framework/            # QA personas, review templates, examples
├── capstone/                # Final challenge + rubric
└── brand/                   # GA compliance checklist
```

## Getting Started

### Prerequisites

- Python 3.10+
- GitHub Copilot access (license required)
- Google Gemini Code Assist (VS Code extension)
- Git

### Setup

```bash
# Clone the workshop repo
git clone git@git.generalassemb.ly:modular-curriculum-all-courses/nypl-ai-engineering-workshop.git

# Clone the sandbox codebase (separate repo, alongside the workshop repo)
git clone https://github.com/NYPL-GA-Training/python-utils.git
cd python-utils

# Set up and verify
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install '.[development]'
python -m pytest           # All tests should pass
```

See [docs/environment-setup.md](docs/environment-setup.md) for detailed Gemini Code Assist and Copilot configuration.

## Development Timeline

| Week | Dates | Focus |
|---|---|---|
| 1 | Feb 18–21 | Repo scaffold, QA framework, sandbox structure |
| 2 | Feb 24–28 | Python sandbox codebase, Labs 1–2, Module 2 content |
| 3 | Mar 2–6 | Labs 3–4, Modules 3–4, capstone challenge |
| 4 | Mar 9–13 | Full dry run, facilitator guide finalization |
| 5 | Mar 16–17 | Final polish, pre-delivery check |
| **Delivery 1** | **Mar 18** | **Cohort 1 (25 engineers)** |
| **Delivery 2** | **Mar 24** | **Cohort 2 (25 engineers)** |

See [docs/timeline.md](docs/timeline.md) for detailed breakdown and [docs/build-tracker.md](docs/build-tracker.md) for current progress.

## SME Review

See [docs/sme-review-guide.md](docs/sme-review-guide.md) for setup instructions, review priorities, and a verification checklist.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for team workflow and conventions.

---

*General Assembly — All rights reserved. For educational use only.*
