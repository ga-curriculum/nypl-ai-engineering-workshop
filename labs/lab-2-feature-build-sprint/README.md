# Lab 2: Feature Build Sprint

## Overview

| Detail | Info |
|---|---|
| **Duration** | 35 minutes |
| **Tools** | Google Gemini + GitHub Copilot |
| **Module** | Module 2: Working with Existing Codebases |
| **QA Persona** | Edge Case Hunter |
| **Depends On** | Sandbox codebase (`sandbox/`) |

## Objective

Build a new feature in the sandbox Python codebase using the dual-tool workflow: Gemini for planning and task decomposition, Copilot for implementation.

## Instructions

### Base Tier (2–5 years experience)

1. Read the feature spec in `starter/`
2. Use Gemini to decompose the feature into implementation steps
3. Implement each step using Copilot inline suggestions
4. Run the existing tests to verify you haven't broken anything: `python -m pytest sandbox/src/tests/`
5. Apply the Edge Case Hunter persona (see `review/`) to your new code

### Intermediate Tier (5–15 years experience)

All of the above, plus:
6. Ask Gemini to identify edge cases specific to your implementation
7. Write tests for at least 3 edge cases Gemini identifies
8. Refactor your implementation based on the edge case analysis

### Stretch Tier (15–25 years experience)

All of the above, plus:
9. Use Gemini to evaluate your task decomposition: "Was this the right breakdown?"
10. Implement error handling using Copilot, then have Gemini review it
11. Write a brief architectural decision record (ADR) for your implementation choices

## Important

Lab 3 builds directly on your Lab 2 output. Make sure your feature is in a working state before moving on. If you're stuck, use the `solution/` folder.

## Review Step

Apply the Edge Case Hunter checklist in `review/` before considering this lab complete.
