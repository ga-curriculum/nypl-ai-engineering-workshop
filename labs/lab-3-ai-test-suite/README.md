# Lab 3: AI Test Suite

## Overview

| Detail | Info |
|---|---|
| **Duration** | 30 minutes |
| **Tools** | Google Gemini Code Assist + GitHub Copilot |
| **Module** | Module 3: Testing and QA with AI |
| **QA Persona** | Test Coverage Analyst |
| **Depends On** | Lab 2 output (or Lab 2 `solution/`) |

## Objective

Generate a pytest test suite for your Lab 2 code using AI tools, then critically evaluate the generated tests for correctness and completeness.

## Instructions

### Base Tier (2–5 years experience)

1. Take your Lab 2 code (or the solution if you didn't finish)
2. Use Copilot to generate a test suite: Add a comment `# Write pytest tests for [function name]` and accept suggestions
3. Run the tests: `python -m pytest -v`
4. Apply the Test Coverage Analyst persona (see `review/`) to evaluate the generated tests
5. Identify at least 1 hallucinated or incorrect test assertion

### Intermediate Tier (5–15 years experience)

All of the above, plus:
6. Use Gemini Code Assist to analyze your test suite: "What's NOT tested in this suite?"
7. Write tests for 3 gaps Gemini Code Assist identifies
8. Ask Gemini Code Assist: "Are any of these tests tautological?" — verify its findings

### Stretch Tier (15–25 years experience)

All of the above, plus:
9. Generate a test suite with Copilot, then a separate one with Gemini Code Assist — compare quality
10. Create a test quality scorecard: rate each test on specificity, coverage, and correctness
11. Write a "test review" prompt that you'd use in your own workflow going forward

## Codebase

This lab uses NYPL's **python-utils** codebase, hosted in NYPL's GitHub organization. See `sandbox/README.md` for setup instructions and the fork URL.

## The Hallucinated Test Exercise

In `starter/` you'll find a test file with intentionally hallucinated tests mixed in with valid ones. Can you spot which tests are asserting behavior that doesn't exist in the source code?

## Review Step

Apply the Test Coverage Analyst checklist in `review/`. The key question: "If all tests pass, am I confident the code works correctly?"
