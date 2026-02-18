# Sandbox — Python Codebase

This is the Python codebase used across all workshop labs. It simulates a realistic application that participants will analyze, extend, test, and review using AI tools.

## Purpose

The sandbox serves as the "existing codebase" that participants work with throughout the workshop:

- **Lab 1**: Analyze this code with Gemini
- **Lab 2**: Build a new feature in this codebase
- **Lab 3**: Generate and evaluate tests for this code
- **Lab 4**: Review and tag code in this codebase
- **Capstone**: Full feature sprint using the sandbox

## Structure

```
sandbox/
├── src/
│   ├── __init__.py
│   ├── core/           # Base application code
│   ├── utils/          # Utility functions
│   └── tests/          # Starter test suite
├── tasks/
│   ├── base/           # Tasks for 2-5 years experience
│   ├── intermediate/   # Tasks for 5-15 years experience
│   └── stretch/        # Tasks for 15-25 years experience
├── requirements.txt
└── README.md           # This file
```

## Setup

```bash
cd sandbox
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

```bash
python -m pytest src/tests/ -v
```

## Design Principles

This codebase is intentionally:
- **Approachable**: Clean enough to understand quickly, but with room for improvement
- **Realistic**: Resembles code participants encounter in real work
- **Extensible**: Designed for participants to add features during labs
- **Testable**: Structured to support meaningful test generation exercises

## TODO

- [ ] Build core application code
- [ ] Create utility modules
- [ ] Write starter test suite
- [ ] Define tiered tasks (base/intermediate/stretch)
- [ ] Write requirements.txt with dependencies
