# Lab 4: Code Review and Tagging

## Overview

| Detail | Info |
|---|---|
| **Duration** | 10 minutes |
| **Tools** | Google Gemini Code Assist (primary) |
| **Module** | Module 4: Transparency and Governance |
| **QA Persona** | Security Auditor |

## Objective

Practice identifying and labeling AI-generated code, then apply a security review as a governance check.

## Instructions

### Base Tier (2–5 years experience)

1. Review the code samples in `starter/`
2. For each sample, label it: **AI-Generated**, **AI-Assisted**, or **Human-Written**
3. Write 1 sentence explaining your reasoning for each label
4. Apply the Security Auditor persona (see `review/`) to the AI-generated samples

### Intermediate Tier (5–15 years experience)

All of the above, plus:
5. For the AI-generated samples, write a PR description that transparently discloses AI usage
6. Suggest what information a teammate would need to review AI-assisted code effectively

### Stretch Tier (15–25 years experience)

All of the above, plus:
7. Draft a 5-point "AI Code Disclosure Policy" for your team
8. Identify scenarios where AI disclosure is critical vs. optional
9. Propose how you'd integrate the QA framework into your team's existing code review process

## Review Step

Apply the Security Auditor checklist in `review/` to all AI-generated code samples. This demonstrates governance through structured review.
