# Exercise 1: Decompose a Feature Request

## Duration: 12 minutes

## Setup
- Open the Gemini Code Assist chat panel in VS Code
- Have the decomposition prompt template from Slide 8 ready

## Feature Request

> **"Add a statistics reporting module"**
>
> The application needs a module that can calculate and display summary statistics (count, mean, median, min, max) for numerical datasets. The module should accept a list of records, compute the statistics, and output a formatted report. It should handle edge cases like empty datasets and non-numeric values gracefully.

## Instructions

### Step 1: Write your own decomposition (2 min)

Without using any AI tools, break this feature request into 5–7 implementation steps.

For each step, write:
- What to implement
- What edge cases to consider

Write your steps here:

| Step | What to implement | Edge cases |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |

### Step 2: Use Gemini Code Assist to decompose it (4 min)

Use the decomposition prompt template:

```
I need to add the following feature to an existing Python codebase:

Add a statistics reporting module that calculates and displays
summary statistics (count, mean, median, min, max) for numerical
datasets. It should accept a list of records, compute statistics,
and output a formatted report.

The codebase currently has:
- A main application module with a CLI entry point
- Dataclass-based models for records
- A utility module with helper functions
- An existing test suite using pytest

Break this into 5–7 implementation steps. For each step:
1. What to implement
2. Which existing files/modules are affected
3. What the inputs and outputs should be
4. What edge cases to consider

Order the steps so each one builds on the previous.
```

Record what Gemini Code Assist produces.

### Step 3: Evaluate AI vs. yours (3 min)

Compare your decomposition with Gemini Code Assist's using this criteria table:

| Criteria | Your Decomposition | Gemini Code Assist | Winner |
|---|---|---|---|
| **Completeness** — Does it cover all aspects of the feature? | | | |
| **Ordering** — Are steps in a logical sequence? | | | |
| **Granularity** — Are steps the right size (not too big, not too small)? | | | |
| **Edge cases** — Are failure modes considered? | | | |
| **Testability** — Can each step be tested independently? | | | |
| **Integration** — Does it account for fitting into existing code? | | | |

### Step 4: Compare with a neighbor (3 min)

Share your table with a neighbor. Discuss:
- What did AI catch that you missed?
- What did you catch that AI missed?
- Would you use AI decomposition in your daily workflow? Why or why not?

## Facilitator Answer Key

A strong decomposition for this feature should include:

1. **Data model** — Define a `StatisticsReport` dataclass with fields for count, mean, median, min, max
2. **Data collection** — Write a function to extract numeric values from records, handling missing/non-numeric values
3. **Calculation logic** — Implement the statistics calculations, guarding against empty datasets and division by zero
4. **Output formatting** — Build a formatter that produces a readable report (and optionally JSON)
5. **Error handling** — Handle edge cases: empty input, all non-numeric values, single-item datasets
6. **Tests** — Write pytest tests covering happy path, empty input, single item, large dataset, non-numeric values
7. **Integration** — Connect to the main application entry point

### Common things AI catches that humans miss:
- Median calculation requires sorting (performance consideration for large datasets)
- Single-item datasets: median = mean = min = max (not really useful statistics)
- Non-numeric values mixed into the dataset need filtering, not crashing
- Output formatting as a separate concern (separation of responsibilities)

### Common things humans catch that AI misses:
- Organizational context ("we already have a utility module this could go in")
- Team conventions ("we use dataclasses, not plain dicts")
- Priority ordering ("error handling matters more than JSON output for v1")
