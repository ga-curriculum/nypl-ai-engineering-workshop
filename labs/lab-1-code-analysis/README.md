# Lab 1: Code Analysis

## Overview

| Detail | Info |
|---|---|
| **Duration** | 30 minutes |
| **Tools** | Google Gemini Code Assist (primary), GitHub Copilot (secondary) |
| **Module** | Module 1: AI as an Engineering Partner |
| **QA Persona** | Code Readability Reviewer |

## Objective

Use Gemini Code Assist's deep analysis capabilities to analyze Python code, identify issues, and generate an improvement plan — then implement the improvements with Copilot.

## Instructions

### Base Tier (2–5 years experience)

1. Open the starter code in `starter/`
2. Use Gemini Code Assist chat to analyze the code: "What are the top 3 issues with this code?"
3. For each issue Gemini Code Assist identifies, use Copilot to implement the fix
4. Apply the Code Readability Reviewer persona (see `review/`) to your final code
5. Document what Gemini Code Assist caught that you might have missed

### Intermediate Tier (5–15 years experience)

All of the above, plus:
6. Ask Gemini Code Assist to propose an architecture improvement for the code
7. Implement the architecture change using Copilot
8. Compare Gemini Code Assist's analysis with your own — where did it add value vs. miss the mark?

### Stretch Tier (15–25 years experience)

All of the above, plus:
9. Write a prompt that gets Gemini Code Assist to generate a full code review document
10. Evaluate the review: What would you accept in a real PR review? What would you push back on?
11. Create your own custom review persona tailored to your domain

## Review Step

After completing your tier, apply the review checklist in `review/` to your final output. This is the Generate > Review > Refine loop in action.

## Solution

Reference solution is in `solution/`. Use it if you get stuck, but try to work through the exercise first.
