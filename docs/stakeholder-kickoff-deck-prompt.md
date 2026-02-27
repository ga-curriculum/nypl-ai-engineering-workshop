# Stakeholder Kickoff Deck — Claude Web Prompt

> Copy everything below the line into Claude Web. It has all the context needed to generate a full slide deck. Ask Claude to create it as a Google Slides artifact or markdown slides.

---

## PROMPT FOR CLAUDE WEB

Create a professional stakeholder kickoff slide deck (Google Slides artifact) for the following workshop. Keep it concise and executive-friendly — this is for the client's engineering leadership, not the participants. Use a clean, modern design. Aim for 12-15 slides.

### PROJECT DETAILS

**Workshop Title:** AI-Assisted Software Engineering Workshop
**Client:** New York Public Library (NYPL) — Digital / Engineering team
**Delivered by:** General Assembly
**Format:** In-person, full-day (6 hours with breaks)
**Dates:** March 18 (Cohort 1, 25 engineers) + March 24 (Cohort 2, 25 engineers)
**Audience:** Software engineers (SE, QA, DevOps), 2–25 years experience
**Tools:** Google Gemini Code Assist + GitHub Copilot
**Language:** Python

### SLIDE OUTLINE

**Slide 1: Title Slide**
- "AI-Assisted Software Engineering Workshop"
- NYPL + General Assembly
- Kickoff Meeting — [today's date]

**Slide 2: Workshop Goals**
- Equip 50 engineers across 2 cohorts to use AI coding tools effectively and responsibly
- Build practical skills with Google Gemini Code Assist and GitHub Copilot
- Establish a shared framework for AI code quality and governance
- Outcome: Engineers leave with a repeatable workflow they can use immediately

**Slide 3: Why These Two Tools?**
- Gemini Code Assist: deep code analysis (1M token context), detailed reasoning, multi-agent planning
- Copilot: fast inline completion, GitHub-native workflow, multi-model flexibility
- Complementary, not competing — "Gemini Code Assist for depth, Copilot for velocity"
- Both already licensed for NYPL engineering team

**Slide 4: Workshop Structure — Day at a Glance**
Table format:
| Time | Block | Duration | Format |
|---|---|---|---|
| 10:00–11:30 | Module 1: AI as an Engineering Partner | 90 min | Lecture + Lab |
| 11:30–1:00 | Module 2: Working with Existing Codebases | 90 min | Lecture + Lab |
| 1:00–2:00 | Lunch | 60 min | — |
| 2:00–3:00 | Module 3: Testing and QA with AI | 60 min | Lecture + Lab |
| 3:00–3:30 | Module 4: Transparency and Governance | 30 min | Lecture + Lab |
| 3:30–4:00 | Wrap-up + Q&A | 30 min | Plenary |

**Slide 5: Module 1 — AI as an Engineering Partner (90 min)**
- Dual-tool framework: when to use Gemini Code Assist vs. Copilot
- High-context prompting: writing prompts that produce usable code on the first try
- Role-based prompting: security engineer, performance engineer, QA engineer perspectives
- Core loop introduced: Generate > Review > Refine
- Lab 1: Analyze Python code with Gemini Code Assist, fix issues with Copilot (tiered difficulty)

**Slide 6: Module 2 — Working with Existing Codebases (90 min)**
- Using AI to navigate and understand unfamiliar code
- Task decomposition: breaking features into AI-sized chunks
- Building features in a real NYPL-adjacent Python codebase
- Lab 2: Feature Build Sprint — participants add a feature to the sandbox codebase using both tools

**Slide 7: Module 3 — Testing and QA with AI (60 min)**
- Generating test suites with AI (and why they need human review)
- Hallucinated assertions: a key risk of AI-generated tests
- QA Framework: 6 reviewer personas + 4 review templates
- Lab 3: Generate, evaluate, and refine a pytest test suite

**Slide 8: Module 4 — Transparency and Governance (30 min)**
- The disclosure spectrum: AI-generated → AI-assisted → AI-reviewed → human-only
- When and how to disclose AI use in PRs, commits, and code comments
- IP and licensing considerations
- 5 essentials of an organizational AI governance policy
- Lab 4: Identify AI-generated vs. human-written code samples + security review

**Slide 9: Capstone Challenge (45 min)**
- Integrates all skills from the day
- Participants work on a real task using both tools
- Must apply the Generate > Review > Refine loop
- Tiered difficulty: base / intermediate / stretch

**Slide 10: QA Framework — Built-in Governance**
- Not just quality — it's a governance mechanism
- 6 QA personas: Security Auditor, Edge Case Hunter, Code Readability Reviewer, Performance Engineer, Junior Dev Reviewer, Test Coverage Analyst
- 4 review templates: Pre-Commit Review, PR Review, Bug Investigation, Refactor Assessment
- Creates audit trail and accountability for AI-generated code
- Participants use these throughout the day and take them back to their teams

**Slide 11: Key Takeaways for Participants**
- A repeatable workflow (Generate > Review > Refine) for using AI tools daily
- Practical experience with Gemini Code Assist + Copilot on Python code
- A QA framework they can adopt on their team immediately
- Clear guidelines for when/how to disclose AI use
- Confidence to use AI tools responsibly and effectively

**Slide 12: Pre-Workshop Requirements**
- All 50 participants need active GitHub Copilot licenses (confirmed — by March 1)
- All 50 participants need Google Gemini Code Assist access (confirmed — by March 1)
- VS Code with Copilot extension installed
- Python 3.10+ environment
- Venue WiFi supporting 25+ simultaneous connections
- Environment setup instructions sent 1 week before each session

**Slide 13: Build Status + Timeline**
- COMPLETE: Module 1 (slides, 3 exercises, lab), Module 4 (slides, 2 exercises, lab), QA Framework (6 personas, 4 templates), Lab 1 & Lab 4, all facilitator docs
- BLOCKED (pending codebase selection): Module 2, Module 3, Lab 2, Lab 3, Capstone, Sandbox codebase
- Deadline: Codebase decision needed by Feb 27 to stay on track for March 18 delivery
- Critical path: Codebase → Module 2 → Lab 2 → Module 3 → Lab 3 → Capstone

**Slide 14: What We Need from NYPL**
- Codebase selection finalized by Feb 27 (criteria shared — Python, pip install, 20-50 files, existing tests, no Docker/DB/external creds)
- Copilot + Gemini Code Assist licenses activated by March 1
- Participant list finalized for both cohorts
- Venue confirmation + WiFi testing

**Slide 15: Questions + Next Steps**
- Next milestone: Codebase finalized → remaining modules built (target: March 7)
- Dry run / content review: March 10-12
- Cohort 1 delivery: March 18
- Cohort 2 delivery: March 24
