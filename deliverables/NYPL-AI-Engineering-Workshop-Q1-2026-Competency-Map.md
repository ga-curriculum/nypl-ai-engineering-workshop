# NYPL — AI-Assisted Software Engineering Workshop — Q1 2026 — Competency Map

---

## Course Summary

| Detail | Info |
|---|---|
| **Course Title** | AI-Assisted Software Engineering Workshop |
| **Client** | New York Public Library (NYPL) |
| **Duration** | 6 hours instruction (7 hours total with lunch) |
| **Delivery Method** | In-person, live instructor, devices required |
| **Learner Persona** | Software engineers (SE, QA, DevOps), 2–25 years experience, Python background |
| **Creation Date** | February 18, 2026 |
| **Customization Level** | L4 (>50% net new build) |
| **Description** | Full-day workshop teaching AI-assisted software engineering using a dual-tool framework (Google Gemini Code Assist + GitHub Copilot) with structured QA review methodology, built on NYPL's own Python codebase. |

---

## Revision History

| Date | Change | Author |
|---|---|---|
| Feb 18, 2026 | Initial scaffold — modules, labs, QA framework | Curriculum Dev |
| Feb 28, 2026 | python-utils sandbox integrated, Labs 1–2 complete | Curriculum Dev |
| Mar 1, 2026 | Labs 2–4, capstone, facilitator guide complete | Curriculum Dev |
| Mar 5, 2026 | Schedule confirmed, Exercise 1 rubric added, cleanup pass | Curriculum Dev |

---

## Competency-to-Module Map

### Competency 1: AI Tool Proficiency

**Definition:** Ability to effectively use AI coding tools (Gemini Code Assist and Copilot) for code generation, analysis, and review.

| Module / Lab | Microlesson | Duration | Tools Required | Learning Objective |
|---|---|---|---|---|
| Module 1 | Dual-Tool Framework | 20 min | Gemini Code Assist, Copilot, VS Code | Explain the complementary strengths of each tool |
| Module 1 | Demo: Email Validation with Both Tools | 5 min | Gemini Code Assist, Copilot | Observe depth vs. velocity in practice |
| Module 2 | Demo: Navigating python-utils | 7 min | Gemini Code Assist, Copilot | Use both tools to explore unfamiliar code |
| Module 3 | Demo: Generate a Test Suite in 60 Seconds | 5 min | Copilot | Generate tests rapidly with AI |
| Capstone | Timed Feature Sprint | 45 min | Gemini Code Assist, Copilot | Apply dual-tool workflow under time pressure |

### Competency 2: Prompt Engineering for Code

**Definition:** Ability to write high-context, structured prompts that produce usable, production-quality code.

| Module / Lab | Microlesson | Duration | Tools Required | Learning Objective |
|---|---|---|---|---|
| Module 1 | Context-Specificity Spectrum | 15 min | — | Understand the difference between vague and high-context prompts |
| Module 1 | Exercise 1: Build a High-Context Prompt | 10 min | Gemini Code Assist, Copilot | Rewrite a vague prompt with specificity, types, edge cases, style |
| Module 1 | Exercise 2: Peer Testing Round-Robin | 10 min | Gemini Code Assist, Copilot | Test prompts across tools and evaluate output quality |
| Module 1 | Exercise 3: Role-Based Prompting | 12 min | Gemini Code Assist | Apply Security, Performance, and QA roles to the same code |
| Module 2 | Task Decomposition Prompt | 8 min | Gemini Code Assist | Break large tasks into 5–7 AI-sized chunks |
| Module 2 | Context Windowing | 5 min | — | Choose what context to include and exclude in prompts |

### Competency 3: Codebase Navigation with AI

**Definition:** Ability to use AI tools to understand, navigate, and extend unfamiliar codebases.

| Module / Lab | Microlesson | Duration | Tools Required | Learning Objective |
|---|---|---|---|---|
| Module 2 | Understanding Code with AI | 20 min | Gemini Code Assist, Copilot | Use AI to analyze architecture and explain functions |
| Module 2 | Demo: Navigating python-utils | 7 min | Gemini Code Assist, Copilot | Gemini Code Assist for the map, Copilot for turn-by-turn |
| Module 2 | Exercise 1: Decompose a Feature Request | 12 min | Gemini Code Assist | Compare human vs. AI task decomposition |
| Lab 2 | Feature Build Sprint | 35 min | Gemini Code Assist, Copilot, python-utils | Extend S3Client with new methods in unfamiliar code |

### Competency 4: AI-Assisted Testing

**Definition:** Ability to generate, evaluate, and refine AI-produced test suites, identifying hallucinated tests.

| Module / Lab | Microlesson | Duration | Tools Required | Learning Objective |
|---|---|---|---|---|
| Module 3 | AI-Generated Tests — Promise and Pitfalls | 8 min | — | Identify three anti-patterns: tautological, hallucinated, over-mocked |
| Module 3 | Test Coverage Analyst Persona | 4 min | — | Apply structured review to AI-generated tests |
| Module 3 | Demo: Finding Hallucinated Assertions | 7 min | — | Walk through hallucinated tests and explain why they're wrong |
| Module 3 | Generate > Review > Refine for Testing | 3 min | — | Apply the core loop specifically to test generation |
| Lab 3 | AI Test Suite — Hallucinated Test Exercise | 30 min | pytest, python-utils | Identify 3 hallucinated tests out of 10, explain each |
| Capstone | Test Phase | 10 min | Copilot, pytest | Generate and review tests for encrypt method |

### Competency 5: Structured Code Review (QA Refinement)

**Definition:** Ability to apply structured QA personas to systematically review AI-generated code before shipping.

| Module / Lab | Microlesson | Duration | Tools Required | Learning Objective |
|---|---|---|---|---|
| Module 1 | Generate > Review > Refine Introduction | 8 min | — | Understand the core loop and why AI output needs structured review |
| Module 1 | Exercise 3: Role-Based Prompting | 12 min | Gemini Code Assist | Apply 3 different review roles to the same code |
| Lab 1 | Code Analysis | 30 min | Gemini Code Assist, Copilot | Apply QA personas to find 16 issues in starter code |
| Lab 2 | Feature Build Sprint (Review Step) | 5 min | — | Apply Edge Case Hunter persona to own code |
| Lab 3 | AI Test Suite (Review Step) | 5 min | — | Apply Test Coverage Analyst persona |
| Capstone | Review Phase | 10 min | Gemini Code Assist | Apply Security Auditor + Edge Case Hunter to encrypt method |

### Competency 6: Responsible AI Use & Governance

**Definition:** Understanding of when and how to disclose AI assistance, IP considerations, and organizational AI governance.

| Module / Lab | Microlesson | Duration | Tools Required | Learning Objective |
|---|---|---|---|---|
| Module 4 | Disclosure Spectrum | 10 min | — | Articulate when to disclose AI assistance in PRs, docs, comments |
| Module 4 | IP and Licensing Considerations | 4 min | — | Identify IP and licensing risks with AI-generated code |
| Module 4 | Organizational AI Policy Essentials | 3 min | — | Describe 5 essentials for an org AI policy |
| Module 4 | NYPL AI Principles & Working Guidelines | 5 min | — | Understand NYPL's specific AI principles and staff guidelines |
| Module 4 | Exercise 1: Disclosure Practice | 5 min | — | Apply disclosure decisions to real-world scenarios |
| Module 4 | Exercise 2: Team AI Policy Draft | 5 min | — | Draft policy elements using NYPL's guidelines as reference |
| Lab 4 | Code Review Tagging | 10 min | — | Distinguish AI-generated, AI-assisted, and human-written code |

---

## Tools Summary

| Tool | Modules Used In | Purpose |
|---|---|---|
| Google Gemini Code Assist | 1, 2, 3, 4, Capstone | Deep analysis, architectural reasoning, QA review |
| GitHub Copilot | 1, 2, 3, Capstone | Inline completion, code generation, test generation |
| VS Code | All | Primary IDE |
| Python 3.10+ | All labs + Capstone | Programming language |
| pytest | Labs 2, 3, Capstone | Test execution and verification |
| python-utils | Labs 1–3, Capstone | Sandbox codebase (S3Client, KmsClient) |

---

## Time Distribution by Competency

| Competency | Lecture/Demo Time | Exercise/Lab Time | Total |
|---|---|---|---|
| AI Tool Proficiency | 37 min | 45 min | 82 min |
| Prompt Engineering | 48 min | 32 min | 80 min |
| Codebase Navigation | 39 min | 47 min | 86 min |
| AI-Assisted Testing | 22 min | 40 min | 62 min |
| Structured Code Review | 20 min | 62 min | 82 min |
| Responsible AI Use & Governance | 27 min | 20 min | 47 min |

> **Note:** Some activities span multiple competencies (e.g., Capstone covers all 6). Times reflect primary competency attribution.

---

*General Assembly — All rights reserved. For educational use only.*
