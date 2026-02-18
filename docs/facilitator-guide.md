# Facilitator Guide — NYPL AI-Assisted Software Engineering Workshop

## Workshop At a Glance

| Detail | Info |
|---|---|
| **Duration** | 6 hours (with breaks) |
| **Audience** | 50 software engineers, 2–25 years experience |
| **Tools** | Google Gemini + GitHub Copilot |
| **Language** | Python |
| **Format** | In-person, devices required |

## Agenda

| Time | Block | Duration | Type |
|---|---|---|---|
| 9:00–9:15 | Welcome and Setup Check | 15 min | Plenary |
| 9:15–10:45 | Module 1: AI as an Engineering Partner | 90 min | Lecture + Lab 1 |
| 10:45–11:00 | Break | 15 min | — |
| 11:00–12:30 | Module 2: Working with Existing Codebases | 90 min | Lecture + Lab 2 |
| 12:30–1:15 | Lunch | 45 min | — |
| 1:15–2:15 | Module 3: Testing and QA with AI | 60 min | Lecture + Lab 3 |
| 2:15–2:30 | Break | 15 min | — |
| 2:30–3:00 | Module 4: Transparency and Governance | 30 min | Lecture + Lab 4 |
| 3:00–3:45 | Capstone Challenge | 45 min | Hands-on |
| 3:45–4:00 | Wrap-up and Q&A | 15 min | Plenary |

## Pre-Workshop Checklist

### 1 Week Before
- [ ] Confirm all 50 participants have GitHub Copilot licenses activated
- [ ] Confirm Gemini access (API keys or workspace access) for all participants
- [ ] Send environment setup instructions ([docs/environment-setup.md](environment-setup.md))
- [ ] Test the sandbox codebase on a clean machine
- [ ] Print participant handouts (if applicable)

### Day Before
- [ ] Verify venue WiFi can handle 50+ simultaneous connections
- [ ] Test screen sharing / projector setup
- [ ] Clone the repo fresh and run through setup to catch any last-minute issues
- [ ] Prepare backup plan for tool access issues (see Contingency Plans below)

### Day Of
- [ ] Arrive 30 min early for setup
- [ ] Have environment-setup.md displayed on screen as participants arrive
- [ ] Do a quick show-of-hands to gauge experience levels (adjust pacing accordingly)

## Module Facilitation Notes

### Module 1: AI as an Engineering Partner (90 min)

**Goal:** Participants understand the dual-tool framework and can use both Gemini and Copilot for basic code generation tasks.

**Key talking points:**
- Gemini excels at reasoning, explanation, and multi-step planning
- Copilot excels at inline code completion and context-aware suggestions
- They complement each other — not competing tools

**Lab 1 notes:**
- Circulate during the lab. Common sticking points: Gemini API auth, Copilot not activating in VS Code
- Remind participants to try all three difficulty tiers (base/intermediate/stretch)
- Time check: allow 30 min for the lab portion

### Module 2: Working with Existing Codebases (90 min)

**Goal:** Participants can use AI tools to navigate, understand, and extend unfamiliar code.

**Key talking points:**
- Task decomposition: break large tasks into AI-sized chunks
- Context matters: show how providing file context improves output
- The sandbox codebase is their "unfamiliar codebase" for this module

**Lab 2 notes:**
- This is the most hands-on module. Participants build a feature in the sandbox.
- Lab 3 builds directly on Lab 2 output — make sure everyone reaches a working state
- Have the solution/ folder ready for anyone who gets stuck

### Module 3: Testing and QA with AI (60 min)

**Goal:** Participants can generate, evaluate, and refine test suites using AI tools.

**Key talking points:**
- AI-generated tests need review — hallucinated assertions are common
- Introduce the QA Refinement Framework (Generate > Review > Refine)
- pytest basics for anyone unfamiliar

**Lab 3 notes:**
- Builds on Lab 2 output. Participants who didn't finish Lab 2 should use the solution/ code.
- Highlight the hallucinated test exercise — this is a memorable teaching moment
- Introduce the first QA persona (test-coverage-analyst)

### Module 4: Transparency and Governance (30 min)

**Goal:** Participants understand responsible AI use in engineering contexts.

**Key talking points:**
- When to disclose AI-assisted code in PRs and documentation
- License and IP considerations
- Organization-level AI governance patterns
- This is intentionally the lightest module — focus on discussion, not exercises

**Lab 4 notes:**
- Code review tagging exercise: participants label AI-generated vs human-written code
- Use this as a segue into the capstone

## Contingency Plans

### Copilot Not Working
- Have participants pair up (one types, one navigates)
- Use instructor screen share for demos
- Copilot chat in browser (github.com/copilot) as fallback

### Gemini Access Issues
- Provide a shared API key for the workshop (rotate after)
- Use Gemini web interface as fallback
- Pre-record demo videos of key Gemini interactions

### WiFi Issues
- Pre-download all dependencies into the sandbox venv
- Have a USB drive with the repo + dependencies
- Key exercises can be done offline with Copilot (inline suggestions don't need internet)

## Post-Workshop

- [ ] Collect participant feedback (survey link TBD)
- [ ] Share repo access with participants for continued practice
- [ ] Send follow-up resources email within 48 hours
