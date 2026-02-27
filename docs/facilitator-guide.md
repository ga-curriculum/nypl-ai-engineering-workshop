# Facilitator Guide — NYPL AI-Assisted Software Engineering Workshop

## Workshop At a Glance

| Detail | Info |
|---|---|
| **Duration** | 10:00 AM – 4:00 PM (5 hours instruction + 1 hour lunch) |
| **Audience** | 25 software engineers per session, 2–25 years experience |
| **Sessions** | Cohort 1: March 18, 2026 (GA Campus, Flatiron NYC — hybrid-capable) |
| | Cohort 2: March 24, 2026 (NYPL Trustee's Room, Bryant Park — NOT hybrid-capable) |
| **Tools** | Google Gemini Code Assist + GitHub Copilot |
| **Language** | Python |
| **Format** | In-person, devices required |

## Agenda

| Time | Block | Duration | Type |
|---|---|---|---|
| 10:00–11:30 | Module 1: AI as an Engineering Partner | 90 min | Lecture + Lab 1 |
| 11:30–1:00 | Module 2: Working with Existing Codebases | 90 min | Lecture + Lab 2 |
| 1:00–2:00 | Lunch | 60 min | — |
| 2:00–3:00 | Module 3: Testing and QA with AI | 60 min | Lecture + Lab 3 |
| 3:00–3:30 | Module 4: Transparency and Governance | 30 min | Lecture + Lab 4 |
| 3:30–4:00 | Wrap-up and Q&A | 30 min | Plenary |

> **Note:** This pacing assumes 5 hours of instruction (10am–4pm with 1 hour lunch). If confirmed as 6 hours of instruction, the additional time can expand Module 4, add a capstone challenge, or provide longer lab sessions.

## Pre-Workshop Checklist

### 1 Week Before
- [ ] Confirm all 25 participants (for this cohort) have GitHub Copilot licenses activated
- [ ] Confirm Gemini Code Assist extension is available for all participants (Google account access verified)
- [ ] Send environment setup instructions ([docs/environment-setup.md](environment-setup.md))
- [ ] Test the sandbox codebase on a clean machine
- [ ] Print participant handouts (if applicable)

### Day Before
- [ ] Verify venue WiFi can handle 25+ simultaneous connections
- [ ] Test screen sharing / projector setup
- [ ] Clone the repo fresh and run through setup to catch any last-minute issues
- [ ] Prepare backup plan for tool access issues (see Contingency Plans below)

### Day Of
- [ ] Arrive 30 min early for setup
- [ ] Have environment-setup.md displayed on screen as participants arrive
- [ ] Do a quick show-of-hands to gauge experience levels (adjust pacing accordingly)

## Module Facilitation Notes

### Module 1: AI as an Engineering Partner (90 min)

**Goal:** Participants understand the dual-tool framework and can use both Gemini Code Assist and Copilot for basic code generation tasks.

**Timing breakdown:**
| Segment | Time |
|---|---|
| Slides 1–5: Dual-tool framework + demo | 20 min |
| Slides 6–8: High-context prompts + role-based prompting | 15 min |
| Exercise 1: Build a High-Context Prompt | 10 min |
| Exercise 2: Peer Testing Round-Robin | 10 min |
| Exercise 3: Role-Based Prompting | 12 min |
| Slides 9–11: Generate > Review > Refine intro | 8 min |
| Transition to Lab 1 | 5 min |
| Lab 1: Code Analysis | 30 min |

**Key talking points:**
- Both tools live in VS Code — Gemini Code Assist and Copilot are both IDE extensions
- Gemini Code Assist excels at deep analysis (1M token context), detailed reasoning, and multi-agent planning
- Copilot excels at fast inline completion, GitHub workflow integration, and multi-model flexibility
- They complement each other — depth vs. velocity, not competing tools
- The Generate > Review > Refine loop is introduced here and used all day

**Demo script (Slide 5):**
- Show the same task (email validation) given to both tools in VS Code
- Gemini Code Assist: Open the chat panel and ask it to reason about what makes a valid email first — point out the detailed, step-by-step response
- Copilot: Type a descriptive comment and let it autocomplete the function — point out the speed
- Point out: Gemini Code Assist gave you depth and reasoning, Copilot gave you code fast — use both

**Exercise 3 answer key:**
- The sample code (`load_config`, `get_users`, `calculate_average_rating`) contains:
  - SQL injection via f-string (Security finds this)
  - Plaintext password loading (Security finds this)
  - `fetchall()` loading all results into memory (Performance finds this)
  - `ZeroDivisionError` on empty reviews list (QA finds this)
  - Missing key `KeyError` crashes (QA finds this)
- All three roles find different issues — this drives the point home

**Lab 1 notes:**
- The starter code (`inventory_manager.py`) has 16 intentional issues across 5 categories
- Circulate during the lab. Common sticking points: Gemini Code Assist extension sign-in, Copilot not activating in VS Code
- Remind participants to try all three difficulty tiers (base/intermediate/stretch)
- Time check: allow 30 min for the lab portion
- Answer key is in `labs/lab-1-code-analysis/solution/issues-found.md`

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

**Optional: NYPL Guest Segment (10–15 min)**
NYPL leadership (Garvita or team lead) may present their internal AI guidelines before the hands-on exercises. If confirmed, position this segment before Exercise 2 (Team AI Policy Draft). Adjust the timing below accordingly — slides can be condensed to make room.

**Timing breakdown:**
| Segment | Time |
|---|---|
| Slides 1–5: Disclosure spectrum + practice | 10 min |
| *(Optional) NYPL AI guidelines presentation* | *10–15 min* |
| Slides 6–8: IP, governance, QA framework as governance | 10 min |
| Slide 9: Quick poll (interactive) | 3 min |
| Transition to Lab 4 | 2 min |
| Lab 4: Code Review Tagging | 10 min |

**Key talking points:**
- The disclosure spectrum: fully AI-generated > AI-assisted > AI-reviewed > human-only
- When to disclose: "Would a reviewer's evaluation change if they knew?"
- License and IP considerations — evolving legal landscape
- The QA Framework is itself a governance mechanism (built-in oversight)
- 5 essentials for an org AI policy: tools, disclosure, review, data, accountability

**Interactive poll (Slide 9):**
- Ask by show of hands: "Does your team have an AI coding policy?"
- "Have you reviewed a PR that was AI-generated without knowing it?"
- This usually sparks good discussion — let it run if energy is there

**Lab 4 notes:**
- 5 code samples in `labs/lab-4-code-review-tagging/starter/code_samples.py`
- Answer key: Samples A, C, E are AI-generated; B is human-written; D is AI-assisted
- The signals: AI code has uniform docstrings, perfect type hints, verbose patterns
- Human code has TODOs with names, informal comments, inconsistent style
- After labeling, participants apply Security Auditor persona to the AI samples
- Use this as a segue into the capstone — "Now use everything you've learned"

## Contingency Plans

### Copilot Not Working
- Have participants pair up (one types, one navigates)
- Use instructor screen share for demos
- Copilot chat in browser (github.com/copilot) as fallback

### Gemini Code Assist Extension Issues
- Have participants sign out and sign back in to the extension
- Check for conflicting AI extensions (disable others temporarily)
- If extension won't load, have participants pair up with a neighbor
- Pre-record demo videos of key Gemini Code Assist interactions as backup

### WiFi Issues
- Pre-download all dependencies into the sandbox venv
- Have a USB drive with the repo + dependencies
- Key exercises can be done offline with Copilot (inline suggestions don't need internet)

## Post-Workshop

- [ ] Collect participant feedback (survey link TBD)
- [ ] Share repo access with participants for continued practice
- [ ] Send follow-up resources email within 48 hours
