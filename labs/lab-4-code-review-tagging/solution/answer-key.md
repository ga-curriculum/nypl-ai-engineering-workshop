# Lab 4: Answer Key — Code Review and Tagging

## Sample Labels

| Sample | Label | Reasoning |
|---|---|---|
| **A** | AI-Generated | Unusually consistent structure: every branch follows the exact same pattern. Perfect docstring with Args/Returns. The `elif` chain checking one condition at a time (instead of collecting all errors) is a common AI pattern — it stops validating after the first error per field. |
| **B** | Human-Written | Informal comments ("just a flat calculation for now"), a TODO with a person's name and date ("asked matt about this 2/3"), no type hints, no docstring, inconsistent formatting. This is clearly working code written quickly by a human. |
| **C** | AI-Generated | Exhaustive docstrings on every method with full Args/Returns/Raises sections. The `__import__("datetime")` hack on line ~130 is a telltale AI artifact — it re-imports datetime inside `__init__` instead of using the already-imported `datetime` module. Perfect consistency across all methods. |
| **D** | AI-Assisted | Functionally correct password hashing using a well-known pattern (pbkdf2_hmac). No docstrings or type hints — suggests a human accepted Copilot's suggestion for a known cryptographic pattern without adding documentation. The code is correct but the human didn't polish it. |
| **E** | AI-Generated | The most obvious AI-generated sample. Extremely thorough docstring (Args with sub-fields documented, Returns with sub-fields, Raises). The implementation is methodical and correct but verbose — a human would likely use `sum()` or a more concise approach. Every edge case is explicitly handled. |

## Signals to Look For

### AI-Generated Code Tells
- Unusually thorough and consistent docstrings (especially Args/Returns/Raises)
- Every function follows the same structural pattern
- Perfect type hints throughout
- Verbose implementations that could be more concise
- "Teaching style" code that's correct but over-documented
- Unusual constructs (like `__import__()` inline)

### Human-Written Code Tells
- Informal comments, TODOs with names/dates
- Inconsistent documentation (some functions documented, others not)
- Pragmatic shortcuts and "good enough" solutions
- Personal style quirks in naming or formatting
- Context that only a team member would know ("asked matt")

### AI-Assisted Code Tells
- Correct algorithmic patterns without personal touches
- Missing documentation on code that uses advanced patterns
- Looks like a "recipe" was followed — correct but impersonal
- Partial polish — some parts clean, others rough

## Security Auditor Review of AI-Generated Samples

### Sample A (validate_user_input)
- **Issue:** Only catches first error per field due to `elif` chain — returns incomplete error lists
- **Issue:** Email validation is too simplistic for production use (should use a library or regex)
- **Issue:** No rate limiting consideration for registration endpoints

### Sample C (BookReservation)
- **Issue:** `__import__("datetime")` is an anti-pattern and could be flagged by linters
- **Issue:** No validation that patron_id and book_isbn follow expected formats
- **Issue:** Status transitions aren't fully guarded (can go from "pending" to "cancelled" but the cancelled state isn't checked in other methods)

### Sample E (process_library_fines)
- **Issue:** Floating point arithmetic for financial calculations — should use `Decimal`
- **Issue:** No pagination or limit on the summary output — could be a memory issue for large patron lists
- **Issue:** `highest_fine` is None when patron_records is empty — downstream consumers need to handle this
