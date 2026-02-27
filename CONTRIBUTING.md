# Contributing to NYPL AI Engineering Workshop

## Team Workflow

### Branching Strategy

- **`main`** — Protected. Requires at least 1 PR review before merge.
- **Feature branches** — Use the naming convention: `feature/<module-or-lab>-<short-description>`
  - Examples: `feature/lab-1-starter-code`, `feature/qa-personas`, `feature/sandbox-core`
- **Fix branches** — `fix/<short-description>`

### Pull Request Process

1. Create a feature branch from `main`
2. Make your changes
3. Open a PR with a clear title and description
4. Tag at least one reviewer
5. Address feedback, then merge

### Commit Messages

Use clear, imperative-style messages:
- `Add Lab 1 starter code and instructions`
- `Update facilitator guide with NYPL timing`
- `Fix sandbox test configuration`

## Content Conventions

### File Naming

- Use kebab-case for all filenames: `facilitator-guide.md`, not `FacilitatorGuide.md`
- Module directories: `module-1-ai-engineering-partner/`
- Lab directories: `lab-1-code-analysis/`

### Markdown Style

- Use ATX headers (`#`, `##`, `###`)
- One sentence per line in source (for cleaner diffs)
- Use fenced code blocks with language identifiers (` ```python `)
- Tables for structured data

### Python Code

- Target Python 3.10+
- Follow PEP 8
- Include type hints on function signatures
- Use `pytest` for all tests
- Keep sandbox code approachable — this is teaching material, not production code

### Tool References

- **Google Gemini Code Assist** and **GitHub Copilot** are the only AI tools referenced in participant-facing materials
- No GPT, OpenAI, ChatGPT, LangChain, or other tool references in exercises or guides
- When showing AI interactions, include both Gemini Code Assist and Copilot examples where applicable

### Tiered Difficulty

Every lab must include tasks at three levels:
- **Base** — For engineers with 2–5 years experience
- **Intermediate** — For engineers with 5–15 years experience
- **Stretch** — For senior engineers with 15–25 years experience

## Content Ownership

Track what you're working on in [docs/build-tracker.md](docs/build-tracker.md). Update status when you start and finish tasks to avoid duplicate effort.
