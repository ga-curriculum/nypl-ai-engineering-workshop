# Module 3: Testing and QA with AI

## Overview

| Detail | Info |
|---|---|
| **Duration** | 60 minutes (30 min lecture + 30 min Lab 3) |
| **Position** | 2:00–3:00 PM |
| **Tools** | Google Gemini Code Assist + GitHub Copilot |
| **Lab** | Lab 3: AI Test Suite |
| **Depends On** | Lab 2 output (or Lab 2 solution/) |

## Learning Objectives

By the end of this module, participants will be able to:
1. Generate a pytest test suite using AI tools
2. Identify hallucinated tests in AI-generated test suites
3. Apply the test coverage analyst persona to evaluate test quality
4. Use the Generate > Review > Refine loop specifically for testing

## Content Outline

### Part 1: AI-Generated Tests — Promise and Pitfalls (15 min)
- Demo: Generate a test suite with Copilot in 60 seconds
- The hallucination problem: tests that pass but don't verify behavior
- Tautological assertions, missing edge cases, over-mocking
- Why "100% coverage" from AI doesn't mean "100% tested"

### Part 2: The Test Coverage Analyst (15 min)
- Introduce the test coverage analyst persona
- Live demo: Apply the persona to an AI-generated test suite
- Walkthrough: Finding hallucinated assertions
- The review checklist: what to verify in every AI-generated test

### Part 3: Lab 3 — AI Test Suite (30 min)
- Generate tests for Lab 2 code, then review with the persona
- Hallucinated test exercise: identify the fake assertions
- See [labs/lab-3-ai-test-suite/](../../labs/lab-3-ai-test-suite/)

## Adapted From

- New content — not directly adapted from source repo
- QA patterns informed by source repo Advanced Prompting module

## Slides

Slide content goes in the `slides/` directory.

## Exercises

In-module exercises go in the `exercises/` directory.
