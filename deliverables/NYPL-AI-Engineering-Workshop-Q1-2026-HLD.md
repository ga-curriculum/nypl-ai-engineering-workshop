# NYPL — AI-Assisted Software Engineering Workshop — Q1 2026 — High-Level Design

---

## Program Title

**AI-Assisted Software Engineering Workshop**

---

## Program Summary

A full-day workshop (6 hours instruction + 1 hour lunch) teaching software engineers to integrate AI tools into professional development workflows using a dual-tool framework (Google Gemini Code Assist + GitHub Copilot) and a structured QA refinement methodology.

---

## Learner Persona

| Attribute | Detail |
|---|---|
| **Role** | Software Engineer, QA Engineer, DevOps Engineer |
| **Experience** | 2 to 25 years |
| **Team Size** | 25 per cohort |
| **Background** | Python experience required; GitHub familiarity expected |
| **Prior AI Tool Experience** | Varies — some participants may have no prior AI coding tool experience |
| **Organization** | New York Public Library (NYPL) — engineering team |
| **Context** | In-person, devices required, working on NYPL's own codebase |

---

## Tools Used in Course

| Tool | Purpose | Access |
|---|---|---|
| **Google Gemini Code Assist** | Deep code analysis, 1M token context, architectural reasoning, multi-agent planning | VS Code extension, Google account |
| **GitHub Copilot** | Inline code completion, fast generation, chat-based coding, GitHub workflow integration | VS Code extension, GitHub license |
| **VS Code** | Primary IDE for all exercises | Participant laptops |
| **Python 3.10+** | Programming language for all labs | Participant laptops |
| **python-utils** | NYPL's Python utility library — the sandbox codebase for all labs | `github.com/NYPL-GA-Training/python-utils` |
| **pytest** | Test framework for Labs 2, 3, and Capstone | Installed via `pip install '.[development]'` |

---

## Learning Outcomes

By the end of this workshop, participants will be able to:

1. Use Gemini Code Assist and Copilot as complementary tools — selecting the right tool for depth vs. velocity
2. Write high-context prompts that produce usable, production-quality code
3. Navigate and extend unfamiliar codebases using AI assistance
4. Generate, evaluate, and refine AI-produced test suites — identifying hallucinated tests
5. Apply the Generate > Review > Refine loop as a standard engineering workflow
6. Use structured QA personas to review AI-generated code before shipping
7. Articulate when and how to disclose AI assistance in professional contexts
8. Align personal AI usage with NYPL's organizational AI guidelines

---

## Module Overview

### Module 1: AI as an Engineering Partner

| | |
|---|---|
| **Duration** | 90 minutes |
| **Problem Addressed** | Engineers don't know how to effectively use AI coding tools, or use only one tool when two would be more effective. Prompts are vague and produce low-quality output. |
| **Solution / Application** | Introduce the dual-tool framework (Gemini Code Assist for depth, Copilot for velocity). Teach high-context prompting and role-based prompting. Establish the Generate > Review > Refine loop. |
| **Lab** | Lab 1: Code Analysis — analyze 107-line Python file with 16 intentional issues |
| **Key Exercises** | Build a high-context prompt; peer testing round-robin; role-based prompting (Security, Performance, QA roles) |

### Module 2: Working with Existing Codebases

| | |
|---|---|
| **Duration** | 90 minutes |
| **Problem Addressed** | Engineers struggle to onboard to unfamiliar codebases. AI tools can accelerate understanding but require structured approaches (task decomposition, context windowing). |
| **Solution / Application** | Use AI to "interview" a codebase — Gemini Code Assist for architectural overview, Copilot for function-level details. Teach task decomposition into AI-sized chunks. |
| **Lab** | Lab 2: Feature Build Sprint — extend `S3Client` with new methods (`list_objects`, `fetch_csv`, `delete_cache`) |
| **Key Exercises** | Task decomposition — compare human vs. AI approaches to breaking down a feature request |

### Module 3: Testing and QA with AI

| | |
|---|---|
| **Duration** | 60 minutes |
| **Problem Addressed** | AI-generated test suites can contain hallucinated assertions — tests that pass but don't verify actual behavior. Engineers need to identify and fix these. |
| **Solution / Application** | Introduce the Test Coverage Analyst persona. Teach the three anti-patterns (tautological assertions, hallucinated behavior, over-mocking). Hands-on hallucinated test identification exercise. |
| **Lab** | Lab 3: AI Test Suite — review 10 "AI-generated" tests, identify 3 hallucinations, explain why they're wrong |
| **Key Exercises** | Lab 3 serves as the exercise (run tests, discover failures, apply persona) |

### Module 4: Transparency and Governance

| | |
|---|---|
| **Duration** | 30 minutes |
| **Problem Addressed** | Organizations lack clear policies on AI-generated code disclosure, IP considerations, and governance. Engineers need frameworks for responsible AI use. |
| **Solution / Application** | Present the disclosure spectrum (AI-generated → AI-assisted → AI-reviewed → human-only). Introduce NYPL's official AI Principles and Working Staff Guidelines. Frame the QA framework as a governance mechanism. |
| **Lab** | Lab 4: Code Review Tagging — label 5 code samples as AI-generated, human-written, or AI-assisted |
| **Key Exercises** | Disclosure practice scenarios; team AI policy draft (references NYPL's real policy) |

---

## Capstone Challenge

| | |
|---|---|
| **Duration** | 45 min sprint + 45 min debrief |
| **Challenge** | Add `encrypt(plaintext, key_id)` to NYPL's `KmsClient` class |
| **Integration** | Combines all workshop skills: dual-tool workflow, task decomposition, AI-assisted testing, QA Refinement Framework |
| **QA Personas** | Security Auditor (primary) + Edge Case Hunter (secondary) |
| **Tiers** | Base: encrypt method; Intermediate: + validation + 5 tests + 2 persona reviews; Stretch: + cross-client `rotate_secret()` function |
| **Assessment** | 100-point rubric covering implementation, testing, and QA review quality |

---

## QA Refinement Framework

The workshop's pedagogical differentiator. Six personas that teach engineers structured review of AI output:

| Persona | Focus Area | Used In |
|---|---|---|
| Security Auditor | Injection, auth, data exposure | Capstone (primary) |
| Edge Case Hunter | Boundary conditions, error paths | Lab 2, Capstone |
| Test Coverage Analyst | Test quality, hallucinated assertions | Lab 3 |
| Code Readability Reviewer | Naming, structure, maintainability | General |
| Performance Engineer | Memory, latency, scaling | General |
| Junior Dev Reviewer | Clarity, documentation, onboarding | General |

**Core methodology:** Generate > Review > Refine

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│ Generate │ →  │  Review  │ →  │  Refine  │
│ (AI)     │    │ (Persona)│    │ (AI+You) │
└──────────┘    └──────────┘    └──────────┘
      ↑                               │
      └───────────────────────────────┘
```

---

## Program Architecture

```
Workshop Flow:

Module 1 (90 min)          Module 2 (90 min)          Lunch
┌─────────────────┐        ┌─────────────────┐        ┌─────┐
│ Dual-Tool       │        │ Codebase        │        │     │
│ Framework       │───────→│ Navigation      │───────→│     │
│ + Prompting     │        │ + Decomposition │        │     │
│ + Lab 1         │        │ + Lab 2         │        │     │
└─────────────────┘        └─────────────────┘        └─────┘
                                                         │
Module 3 (60 min)          Module 4 (30 min)             │
┌─────────────────┐        ┌─────────────────┐           │
│ Testing & QA    │        │ Transparency    │←──────────┘
│ + Hallucination │───────→│ + Governance    │
│ Detection       │        │ + NYPL AI Policy│
│ + Lab 3         │        │ + Lab 4         │
└─────────────────┘        └─────────────────┘
                                    │
Capstone (45 min)          Wrap-up (45 min)
┌─────────────────┐        ┌─────────────────┐
│ KMS Encryption  │        │ Debrief         │
│ Feature Sprint  │───────→│ Key Takeaways   │
│ (All skills)    │        │ Q&A             │
└─────────────────┘        └─────────────────┘
```

---

## NYPL-Specific Integration

- **Codebase:** All labs use NYPL's `python-utils` library — real code, not toy examples
- **AI Guidelines:** Module 4 incorporates NYPL's official *AI Principles & Working Staff Guidelines* (CONFIDENTIAL)
- **Guest Speaker:** Optional 10–15 min slot for NYPL leadership in Module 4
- **Values Alignment:** QA framework maps to NYPL's principles of accountability, transparency, and human-first approach

---

*General Assembly — All rights reserved. For educational use only.*
