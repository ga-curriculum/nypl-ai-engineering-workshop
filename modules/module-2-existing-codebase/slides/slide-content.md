# Module 2: Working with Existing Codebases — Slide Content

> These are the content notes for each slide. Convert to your slide deck tool (Google Slides, Keynote, etc.) using GA templates.

---

## Slide 1: Title

**Working with Existing Codebases**
Module 2 | 90 minutes

---

## Slide 2: Learning Objectives

By the end of this module, you will:
1. Use AI tools to navigate and understand an unfamiliar codebase
2. Decompose a feature request into AI-appropriate subtasks
3. Build a new feature in an existing codebase using the dual-tool workflow
4. Apply the edge-case hunter persona to your own code

---

## Slide 3: The Challenge of Unfamiliar Code

Every engineer has stared at an unfamiliar codebase and thought: *"Where do I even start?"*

AI tools let you **interview the codebase** — ask questions, get explanations, and build a mental model faster than reading files one by one.

### Two tools, two levels of understanding:

| What you need | Tool | Why |
|---|---|---|
| Big-picture architecture | Gemini Code Assist | 1M token context — can analyze entire modules and their relationships |
| Function-level explanation | Copilot | Fast, focused explanations in the editor context |

**Think of it this way:** Gemini Code Assist gives you the map. Copilot gives you turn-by-turn directions.

---

## Slide 4: Asking the Right Questions

The quality of AI's answers depends on the quality of your questions.

### Question types for exploring unfamiliar code:

| Question Type | Example Prompt (Gemini Code Assist) | Example Prompt (Copilot) |
|---|---|---|
| Architecture | "Explain the overall architecture of this project. What are the main modules and how do they interact?" | "What does this module do and what are its dependencies?" |
| Dependencies | "Map the dependency graph for this project. Which modules depend on which?" | "What does this import do and where is it defined?" |
| Function purpose | "Explain what this function does, its parameters, return value, and any side effects" | "Explain this function" (highlight + chat) |
| Patterns | "What design patterns are used in this codebase? Show examples of each" | "Is this following a factory pattern? How?" |
| Data flow | "Trace the flow of data from user input to database storage in this module" | "Where does this variable get modified?" |

**Key insight:** Start with broad architectural questions in Gemini Code Assist, then drill into specifics with Copilot.

---

## Slide 5: Demo — Navigating the Sandbox Codebase

**Two-step exploration:**

### Step 1: Gemini Code Assist — Big-picture analysis
```
I'm new to this Python codebase. Give me an architectural overview:
1. What are the main modules and what does each one do?
2. How do the modules interact with each other?
3. What are the key entry points?
4. Are there any external dependencies I should know about?
```
*Result: Gemini Code Assist maps the terrain — modules, relationships, entry points.*

### Step 2: Copilot — Drill into a specific function
```python
# Explain what this function does, what each parameter means,
# and what edge cases I should be aware of
```
*(Highlight a function → right-click → Copilot: Explain)*

*Result: Copilot gives you the focused, line-by-line understanding.*

**Gemini Code Assist gave us the map. Copilot gives us turn-by-turn directions.**

---

## Slide 6: Context Windowing

Not every question needs the full codebase. Match the context you provide to the scope of your question.

### Three levels of context:

| Level | What to include | When to use | Example |
|---|---|---|---|
| **Minimal** | Just the function or class | Simple explanations, quick fixes | "What does this function return?" |
| **Module** | The file + its direct imports | Understanding behavior, writing tests | "How does this function interact with the database layer?" |
| **Architectural** | Multiple files, project structure | Planning features, understanding data flow | "How would I add a new API endpoint to this system?" |

**Tip:** Start narrow, widen as needed. You can always add more context in follow-up messages.

### Anti-pattern: The context dump
```
Here's my entire codebase [5,000 lines]. What does it do?
```
This overwhelms even large context windows. **Always pair context with a specific question.**

---

## Slide 7: From Understanding to Action — Task Decomposition

You understand the codebase. Now you need to build something in it.

**The problem:** "Add a statistics reporting module" is too big for a single AI prompt.

**The solution:** Break large tasks into **5–7 focused subtasks** that AI can handle one at a time.

```
Large task
    ├── Subtask 1: Define the data model
    ├── Subtask 2: Write the data collection function
    ├── Subtask 3: Implement the aggregation logic
    ├── Subtask 4: Build the output formatter
    ├── Subtask 5: Add error handling
    ├── Subtask 6: Write tests
    └── Subtask 7: Integrate with the main module
```

**Why this works:** Each subtask is concrete, testable, and fits within a single AI interaction.

---

## Slide 8: The Decomposition Prompt

Use this reusable template to decompose any feature request:

```
I need to add the following feature to an existing Python codebase:

[Feature description]

The codebase currently has:
[Brief description of relevant existing code]

Break this into 5–7 implementation steps. For each step:
1. What to implement
2. Which existing files/modules are affected
3. What the inputs and outputs should be
4. What edge cases to consider

Order the steps so each one builds on the previous.
```

### Example output (for "add a statistics reporting module"):
| Step | Task | Files Affected | Key Consideration |
|---|---|---|---|
| 1 | Define a `StatisticsReport` dataclass | `models.py` | Include fields for count, mean, median, min, max |
| 2 | Write `collect_data()` to gather raw records | `statistics.py`, `database.py` | Handle empty datasets |
| 3 | Implement `calculate_stats()` aggregation | `statistics.py` | Guard against division by zero |
| 4 | Build `format_report()` output formatter | `statistics.py` | Support both text and JSON output |
| 5 | Add error handling and logging | `statistics.py` | Log failures without crashing |
| 6 | Write pytest tests for each function | `tests/test_statistics.py` | Test with empty, single-item, and large datasets |
| 7 | Integrate with the main application | `main.py` | Add CLI flag or config option to trigger reports |

---

## Slide 9: Context Matters — Same Task, Different Context

The same request produces dramatically different results depending on the context you provide.

### Without context:
```
Write a function that calculates statistics for a dataset.
```
*Result: Generic function, doesn't fit your codebase, uses different patterns and naming.*

### With context:
```
Write a function that calculates statistics for a dataset.

This is part of a Python project that:
- Uses dataclasses for models (see: @dataclass class Record)
- Follows the pattern in existing modules: function takes a
  list of Records, returns a typed result
- Uses logging (import logging; logger = logging.getLogger(__name__))
- Handles errors by raising ValueError with descriptive messages

The function should follow the same patterns. Here's an example
from the existing codebase:

[paste an existing function that follows the pattern]
```
*Result: Function matches your codebase style, uses your patterns, integrates cleanly.*

**The takeaway:** 2 minutes of context saves 20 minutes of refactoring.

---

## Slide 10: Exercise — Decompose a Feature Request

**Duration: 12 minutes**

You'll practice task decomposition using the template from Slide 8.

1. Read the feature request in the exercise handout
2. Write your own decomposition first (no AI)
3. Use Gemini Code Assist to decompose the same feature
4. Compare: What did AI catch that you missed? What did you catch that AI missed?

See the exercise handout for full instructions.

---

## Slide 11: Lab 2 Preview

**Lab 2: Feature Build Sprint** (35 minutes)

You'll use the dual-tool workflow to build a feature in the sandbox codebase.

Three tiers:
- **Base:** Decompose a feature, implement with Copilot, run existing tests
- **Intermediate:** Add edge case analysis with Gemini Code Assist, write edge case tests
- **Stretch:** Evaluate your own decomposition, implement error handling, write an ADR

**Note:** Lab 3 uses the *original* `s3_client.py` (not your extensions), so you can proceed even if you didn't finish all tiers. Make sure existing tests still pass before moving on.

---

## Slide 12: Recap

What we covered:
1. AI tools let you "interview" an unfamiliar codebase — Gemini Code Assist for the big picture, Copilot for details
2. Ask the right questions: architecture first, then drill down
3. Match your context window to your question scope — start narrow, widen as needed
4. Break large tasks into 5–7 AI-sized subtasks before prompting
5. Providing codebase context dramatically improves AI output quality

**Up next:** Lab 2 — build a feature using everything you've learned.
