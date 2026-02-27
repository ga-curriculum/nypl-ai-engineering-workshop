# Module 4: Transparency and Governance — Slide Content

> These are the content notes for each slide. Convert to your slide deck tool using GA templates.

---

## Slide 1: Title

**Transparency and Governance**
Module 4 | 30 minutes

---

## Slide 2: Learning Objectives

By the end of this module, you will:
1. Know when and how to disclose AI-assisted code in pull requests
2. Understand IP and licensing considerations for AI-generated code
3. Apply a labeling system to distinguish AI-generated from human-written code
4. Describe what an organizational AI governance policy should cover

---

## Slide 3: The Disclosure Spectrum

Not all AI-assisted code is the same. There's a spectrum:

| Level | Description | Example |
|---|---|---|
| **Fully AI-generated** | AI wrote the code, human reviewed it | "Generate a pytest suite for this module" |
| **AI-assisted** | Human wrote the code with AI suggestions | Copilot autocomplete accepted inline |
| **AI-reviewed** | Human wrote the code, AI reviewed it | Gemini Code Assist review before PR |
| **Human-only** | No AI tools involved | Manual coding, no Copilot active |

**Question for the room:** Where does your team draw the disclosure line?

---

## Slide 4: When Should You Disclose?

### Always disclose:
- Fully AI-generated functions or modules
- AI-generated test suites (especially important — tests are trust infrastructure)
- Architecture or design decisions that came from AI reasoning

### Use judgment:
- Copilot inline completions (single lines, boilerplate)
- AI-assisted refactoring where you directed every step

### The test: Would a reviewer's evaluation change if they knew AI generated this?
If yes, disclose.

---

## Slide 5: What Disclosure Looks Like in Practice

### In a PR description:
```
## AI Assistance

- `utils/validators.py` — Functions generated with Gemini Code Assist,
  reviewed and modified by hand
- `tests/test_validators.py` — Test suite generated with
  Copilot, reviewed with Test Coverage Analyst persona
- All other changes are human-written
```

### In code comments (for significant blocks):
```python
# AI-generated (Gemini Code Assist) — reviewed and edge cases added manually
def validate_isbn(isbn: str) -> bool:
    ...
```

### In commit messages:
```
Add user validation module

Generated initial implementation with Gemini Code Assist, refined after
security auditor review. Test suite generated with Copilot
and verified against edge case checklist.
```

---

## Slide 6: IP and Licensing Considerations

### What to be aware of:

- **AI training data:** Models are trained on open-source code. Generated code may resemble copyrighted source material.
- **License compliance:** If AI generates code that mirrors a GPL-licensed project, your project may have obligations.
- **Ownership:** Most legal interpretations currently treat AI-generated code as belonging to the person/org that directed its creation — but this is evolving.

### Practical guidelines:
- Review AI-generated code for originality, especially for core algorithms
- Don't rely on AI for license-critical code without review
- Follow your organization's IP policy (when one exists)
- When in doubt, rewrite the critical section by hand

---

## Slide 7: The QA Framework as Governance

You've been using the QA Framework all day. It's not just a quality tool — it's a governance mechanism.

**Generate > Review > Refine = built-in oversight**

| Governance Need | How the Framework Addresses It |
|---|---|
| Code quality | QA personas catch bugs before they ship |
| Security | Security Auditor persona checks every lab |
| Transparency | The process itself documents how code was produced |
| Accountability | Review artifacts show what was checked and by whom |
| Auditability | Review templates create a paper trail |

**The framework makes responsible AI use a process, not a policy memo.**

---

## Slide 8: Building an AI Governance Policy

If your team doesn't have one yet, here are the 5 essentials:

1. **Approved tools** — Which AI tools are sanctioned for use?
2. **Disclosure requirements** — When must AI assistance be disclosed?
3. **Review standards** — What review is required for AI-generated code?
4. **Data handling** — What code/data can be shared with AI tools?
5. **Accountability** — Who is responsible for AI-generated code quality?

**Key principle:** The engineer who commits the code owns it, regardless of how it was generated.

---

## Slide 9: Quick Poll

(Interactive — show of hands or chat)

1. Does your team currently have an AI coding policy? (Yes / No / Informal)
2. Have you ever reviewed a PR that was AI-generated without knowing it?
3. Would you feel comfortable telling your team lead that a critical function was AI-generated?

---

## Slide 10: Lab 4 Preview

**Lab 4: Code Review and Tagging** (10 minutes)

You'll review code samples and label each one:
- AI-Generated
- AI-Assisted
- Human-Written

Then apply the Security Auditor persona to the AI-generated samples.

See `labs/lab-4-code-review-tagging/` for instructions.

---

## Slide 11: Recap

What we covered:
1. The disclosure spectrum: fully AI-generated → human-only
2. When and how to disclose AI in PRs, commits, and comments
3. IP and licensing awareness
4. The QA Framework doubles as a governance mechanism
5. Five essentials for an organizational AI policy

**The engineer who commits the code owns it. AI is the tool, you're the author.**

**Up next:** Lab 4 — then the Capstone Challenge.
