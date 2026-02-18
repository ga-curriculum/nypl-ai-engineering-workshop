# Module 1: AI as an Engineering Partner — Slide Content

> These are the content notes for each slide. Convert to your slide deck tool (Google Slides, Keynote, etc.) using GA templates.

---

## Slide 1: Title

**AI as an Engineering Partner**
Module 1 | 90 minutes

---

## Slide 2: Learning Objectives

By the end of this module, you will:
1. Use Google Gemini and GitHub Copilot as complementary engineering tools
2. Write high-context prompts that produce usable code on the first try
3. Apply role-based prompting to get specialized output (security, performance, QA)
4. Understand the Generate > Review > Refine loop that underpins the entire workshop

---

## Slide 3: Why Two Tools?

**Google Gemini** and **GitHub Copilot** are not competing tools — they have complementary strengths.

| Capability | Gemini | Copilot |
|---|---|---|
| Reasoning and explanation | Strong | Moderate |
| Multi-step planning | Strong | Moderate |
| Inline code completion | N/A | Strong |
| Context-aware suggestions in-editor | N/A | Strong |
| Code review and analysis | Strong | Good (via chat) |
| Generating code from scratch | Good | Strong (in-editor) |

**The dual-tool workflow:** Gemini for thinking, Copilot for building.

---

## Slide 4: When to Use Which Tool

### Use Gemini when you need to:
- Understand unfamiliar code ("Explain what this function does and why")
- Plan before coding ("Break this feature into implementation steps")
- Review and critique ("Find edge cases in this function")
- Reason about architecture ("What are the trade-offs of approach A vs B?")

### Use Copilot when you need to:
- Write code in your editor (inline suggestions)
- Complete boilerplate quickly (type a comment, get the implementation)
- Generate tests from existing code
- Refactor with chat guidance while staying in your IDE

---

## Slide 5: Demo — Same Task, Two Tools

**Task:** Write a Python function that validates an email address.

### Gemini approach (reasoning first):
```
I need a Python function that validates email addresses for a
user registration system. Before writing code, help me think
through: What constitutes a valid email? What edge cases should
I handle? What's the simplest approach that's production-safe?
```

### Copilot approach (code-first):
```python
# Validate an email address for user registration.
# Return (is_valid: bool, error: str | None).
# Handle: empty input, missing @, invalid domain, length > 254
def validate_email(email: str) -> tuple[bool, str | None]:
```

**Key point:** Gemini helped us think. Copilot helped us build. Both are valuable.

---

## Slide 6: The Context-Specificity Spectrum

Prompt quality exists on a spectrum from vague to high-context.

### Bad prompt:
```
Write me a Python function.
```

### Better prompt:
```
Write a function that sorts a list.
```

### Good prompt:
```
Write a Python function called sort_users_by_age that takes
a list of user dictionaries (each with 'name' and 'age' keys)
and returns a new list sorted by age ascending. Handle the case
where 'age' might be missing or non-numeric. Include type hints.
```

**The pattern:** Specify the language, function name, input/output types, edge cases, and style expectations.

---

## Slide 7: Anatomy of a High-Context Prompt

A strong engineering prompt includes:

1. **Role** (optional but powerful) — "You are a senior Python developer..."
2. **Task** — What you want done
3. **Context** — Technology stack, constraints, what already exists
4. **Input/Output** — Expected types, formats, examples
5. **Edge cases** — What should happen when things go wrong
6. **Style** — Naming conventions, patterns, type hints

```
You are a senior Python developer working on a FastAPI application.

Write a function called `get_active_users` that queries a list of
user dictionaries and returns only users where 'is_active' is True.

Input: list[dict] where each dict has keys 'id', 'name', 'is_active'
Output: list[dict] containing only active users
Edge cases: Handle empty list, missing 'is_active' key (treat as inactive)
Style: Include type hints, use list comprehension, add a docstring
```

---

## Slide 8: Role-Based Prompting

Assigning a role changes the lens through which AI evaluates your code.

### Security Engineer
```
You are a security engineer reviewing this Python code before
deployment. Check for: input validation gaps, injection risks,
hardcoded secrets, and authentication issues.
```

### Performance Engineer
```
You are a performance engineer. Analyze this function for:
time complexity, unnecessary memory allocation, and N+1
query patterns. Suggest optimizations.
```

### QA Engineer
```
You are a QA engineer. Generate edge case tests for this function.
Focus on: boundary values, empty inputs, type mismatches, and
error conditions.
```

**These roles map directly to our QA Framework personas.** You'll use them all day.

---

## Slide 9: Live Exercise Preview — Build a High-Context Prompt

In a moment, you'll:
1. Take a vague prompt and rewrite it as a high-context prompt
2. Test it in Gemini
3. Exchange it with a peer for feedback
4. Apply a role-based lens to get a different perspective

See the exercise handout for details.

---

## Slide 10: The Generate > Review > Refine Loop

This is the most important concept in the workshop.

```
Generate  ──>  Review  ──>  Refine
   │              │             │
   │         Apply a QA    Feed feedback
   │         persona       back into the
   Use AI                  tool and iterate
   to write
   code
```

**AI output is a draft, not a deliverable.**

Every lab today follows this loop. By the capstone, it should be muscle memory.

---

## Slide 11: Introducing the Pre-Commit Review

Before you commit any AI-generated code, run this check:

```
Review this code before I commit it. Check for:
1. No hardcoded secrets or credentials
2. No debug code (print statements, breakpoints)
3. Functions have type hints and docstrings
4. Error handling is appropriate
5. No commented-out code blocks
6. Variable names are clear and consistent

Respond: PASS or HOLD with issues to fix.
```

You'll use this template starting in Lab 1 and throughout the day.

---

## Slide 12: Lab 1 Preview

**Lab 1: Gemini Reasoning** (30 minutes)

You'll use Gemini to analyze Python code, identify issues, and plan improvements — then use Copilot to implement fixes.

Three tiers:
- **Base:** Use Gemini to find top 3 issues, fix with Copilot
- **Intermediate:** Add architecture improvement
- **Stretch:** Generate a full code review document and evaluate it

See `labs/lab-1-gemini-reasoning/` for instructions.

---

## Slide 13: Recap

What we covered:
1. Gemini for reasoning + Copilot for building = dual-tool workflow
2. High-context prompts produce better code faster
3. Role-based prompting gives specialized perspectives
4. Generate > Review > Refine is the loop we use all day
5. Pre-commit review catches common AI mistakes

**Up next:** Lab 1 — put it into practice.
