# QA Refinement Framework

The QA Refinement Framework is the key differentiator of this workshop. It teaches engineers to treat AI-generated code as a **draft, not a deliverable** by embedding structured review into every lab.

## The Loop: Generate > Review > Refine

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│ Generate │ ──> │  Review  │ ──> │  Refine  │
│          │     │          │     │          │
│ Use AI   │     │ Apply QA │     │ Feed     │
│ to write │     │ persona  │     │ feedback │
│ code     │     │ review   │     │ back in  │
└──────────┘     └──────────┘     └─────┬────┘
                                        │
                                        └──> Repeat until quality bar is met
```

1. **Generate** — Use Gemini or Copilot to produce code or a solution
2. **Review** — Invoke a QA persona to evaluate the output against specific criteria
3. **Refine** — Feed the review feedback back into the tool and iterate

## QA Personas

Each persona evaluates code through a specific lens:

| Persona | Focus Area | Best Used For |
|---|---|---|
| [Security Auditor](personas/security-auditor.md) | Vulnerabilities, injection, auth | Any code handling user input or auth |
| [Edge Case Hunter](personas/edge-case-hunter.md) | Boundary conditions, failure modes | Logic-heavy code, data processing |
| [Code Readability Reviewer](personas/code-readability-reviewer.md) | Clarity, naming, structure | All code — especially AI-generated |
| [Performance Engineer](personas/performance-engineer.md) | Efficiency, memory, scaling | Data processing, API endpoints |
| [Junior Dev Reviewer](personas/junior-dev-reviewer.md) | Understandability, maintainability | Shared/team code, library code |
| [Test Coverage Analyst](personas/test-coverage-analyst.md) | Test completeness, edge cases | Test suites, QA exercises |

## How Personas Are Used in Labs

Every lab's `review/` folder contains:
- A **persona prompt** specific to that lab's focus
- An **evaluation checklist** the persona uses
- A **feedback template** structuring the review output
- **Example catches** showing what the persona typically flags

| Lab | Primary Persona | Why |
|---|---|---|
| Lab 1: Gemini Reasoning | Code Readability Reviewer | Focus on clear, well-structured output |
| Lab 2: Feature Build Sprint | Edge Case Hunter | New feature code needs boundary testing |
| Lab 3: AI Test Suite | Test Coverage Analyst | Directly evaluating test quality |
| Lab 4: Code Review Tagging | Security Auditor | Full review lens for the tagging exercise |
| Capstone | All personas | Full Generate > Review > Refine cycle |

## Templates

Reusable review templates for common engineering workflows:

- [Pre-Commit Review](templates/pre-commit-review.md) — Run before every commit
- [PR Review Prompt](templates/pr-review-prompt.md) — AI-assisted pull request review
- [Bug Investigation](templates/bug-investigation.md) — Systematic AI-assisted debugging
- [Refactor Assessment](templates/refactor-assessment.md) — Evaluate refactoring decisions

## Examples

- [Example Review Session](examples/example-review-session.md) — Full walkthrough of Generate > Review > Refine
- [Common Catches](examples/common-catches.md) — Real examples of what personas flag in AI-generated code

## Why This Matters

NYPL's goals: **fewer production bugs** and **increased correct tool use**. The refinement layer directly addresses both by making structured review a habit, not an afterthought. Engineers leave this workshop with a repeatable process, not just tool familiarity.
