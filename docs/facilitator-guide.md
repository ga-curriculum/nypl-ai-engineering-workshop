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

**Timing breakdown:**
| Segment | Time |
|---|---|
| Slides 1–4: Unfamiliar code + asking the right questions | 8 min |
| Slide 5: Demo — navigating the sandbox codebase | 7 min |
| Slide 6: Context windowing | 5 min |
| Slides 7–8: Task decomposition + decomposition prompt | 8 min |
| Slide 9: Context matters — same task, different context | 4 min |
| Exercise 1: Decompose a Feature Request | 12 min |
| Slides 11–12: Lab preview + recap | 3 min |
| Transition to Lab 2 | 3 min |
| Lab 2: Feature Build Sprint | 35 min |
| Lab 2 Debrief | 5 min |

**Key talking points:**
- AI lets you "interview" an unfamiliar codebase — Gemini Code Assist for the big picture, Copilot for function-level details
- Task decomposition: break large tasks into 5–7 AI-sized chunks
- Context matters: show how providing file context improves output quality dramatically
- The sandbox codebase is their "unfamiliar codebase" for this module

**Demo script (Slide 5):**
- Step 1: Open Gemini Code Assist chat and ask for an architectural overview of python-utils — point out how the 1M token context lets it see entire modules at once
- Step 2: Open `s3_client.py`, highlight the `fetch_cache` method, and use Copilot to explain it line by line
- Bridge the two: "Gemini Code Assist gave us the map, Copilot gives us turn-by-turn directions"

**Exercise 1 notes:**
- The exercise compares human vs. AI task decomposition — this is not about AI being better, it's about finding complementary strengths
- Common observation: AI is more systematic about edge cases, humans are better at organizational context and priorities
- Allow 3 min for neighbor discussion — this usually generates good energy

**Lab 2 notes:**
- This is the most hands-on module. Participants extend `s3_client.py` in python-utils with new methods (`list_objects`, `fetch_csv`, `delete_cache`).
- The feature spec is in `labs/lab-2-feature-build-sprint/starter/feature-spec.md`
- Remind participants: the file is only ~65 lines with 2 existing tests (`tests/test_s3_client.py`) — manageable scope
- Lab 3 uses the *original* `s3_client.py` (not Lab 2 extensions), so participants can proceed even if they didn't finish all tiers
- Have the solution ready (`labs/lab-2-feature-build-sprint/solution/s3_client_extended.py`) for anyone who gets stuck
- Introduce the Edge Case Hunter persona during the debrief — it's the review checklist for Lab 2

### Module 3: Testing and QA with AI (60 min)

**Goal:** Participants can generate, evaluate, and refine test suites using AI tools.

**Timing breakdown:**
| Segment | Time |
|---|---|
| Slides 1–2: Title + learning objectives | 1 min |
| Slide 3: Demo — generate a test suite in 60 seconds | 5 min |
| Slides 4–5: Tests that lie + what makes a good test | 8 min |
| Slide 6: Introducing the Test Coverage Analyst persona | 4 min |
| Slide 7: Demo — finding hallucinated assertions | 7 min |
| Slide 8: Generate > Review > Refine for testing | 3 min |
| Slides 9–10: Lab preview + recap | 2 min |
| Lab 3: AI Test Suite | 30 min |

**Key talking points:**
- AI-generated tests need review — hallucinated assertions are the #1 risk
- Three anti-patterns: tautological assertions, hallucinated behavior, over-mocking
- The Test Coverage Analyst persona systematically catches these issues
- Use Gemini Code Assist for test review (1M context holds source + tests together), Copilot for test generation
- Generate > Review > Refine applies to testing: Copilot generates, Gemini Code Assist reviews, Copilot fills gaps

**Demo script (Slide 7):**
- Show the `get_active_users` function and its 5 AI-generated tests
- Walk through each test — first 3 are good, tests 4 and 5 are hallucinated
- Test 4 (sorts by name): the function doesn't sort — this might pass by coincidence with certain input order
- Test 5 (excludes deleted users): the function doesn't check the 'deleted' field
- Ask the room: "Would you have caught these in a code review?" — this is the memorable moment

**Lab 3 notes:**
- The hallucinated test exercise targets the *original* `s3_client.py` (not Lab 2 extensions) — participants do NOT need to have finished Lab 2
- The starter file (`labs/lab-3-ai-test-suite/starter/test_s3_client_review.py`) has 10 tests; 3 are hallucinated (Tests 4, 7, 9)
- Participants copy the test file into `python-utils/tests/` and run it — 7 tests pass, 3 fail
- **This is the memorable teaching moment** — walk the room and let participants discover the failures, then discuss why
- Hallucination types: assumed retry logic (Test 4), assumed JSON error handling (Test 7), invented gzip compression (Test 9)
- Answer key: `labs/lab-3-ai-test-suite/solution/hallucination-answers.md`
- The Test Coverage Analyst persona is the review checklist for this lab
- Remind participants: "If all tests pass, am I confident the code works correctly?"

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
