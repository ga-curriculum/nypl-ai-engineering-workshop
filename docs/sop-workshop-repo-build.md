# SOP: Building a Workshop Repo with Claude Code

Standard operating procedure for LEDs building client workshop repositories using Claude Code CLI. Based on the process used to build the NYPL AI-Assisted Software Engineering Workshop (Feb 2026).

---

## Prerequisites

Before starting, you need:
- [ ] **Claude Code CLI** installed (`npm install -g @anthropic-ai/claude-code` or via your preferred method)
- [ ] **GitHub CLI** (`gh`) installed (`brew install gh`)
- [ ] **Git** installed and configured
- [ ] `gh` authenticated to the target GitHub host (e.g., `gh auth login`)
- [ ] A **briefing document** with: client name, audience, tools, modules, timeline, and what to carry over from source repos

## Phase 1: Setup and Auth (10 min)

### 1.1 Install GitHub CLI (if needed)
```
brew install gh
```

### 1.2 Authenticate to GitHub
```
gh auth login
```
Choose HTTPS and browser login. Verify with:
```
gh auth status
```

### 1.3 Clone source repo(s)
If adapting from an existing workshop, clone the source locally first:
```
git clone https://github.com/[org]/[source-repo].git ~/Documents/GitHub/[source-repo]
```
Claude Code will read from this to adapt content.

## Phase 2: Repo Creation and Scaffold (15 min)

### 2.1 Start Claude Code
Navigate to your GitHub working directory and start Claude Code:
```
cd ~/Documents/GitHub
claude
```

### 2.2 Provide the briefing
Paste your briefing document into Claude Code. Include:
- Workshop name, client, audience size, experience range
- Tools being taught (e.g., Gemini Code Assist + Copilot)
- Programming language
- Module structure with timing
- What to carry over from source repos (and what NOT to carry over)
- Desired repo structure (or let Claude propose one)

### 2.3 Claude Code will:
1. **Create the repo** on GitHub Enterprise using `gh repo create`
2. **Scaffold the full directory structure** (modules, labs, docs, etc.)
3. **Write core files**: README, CONTRIBUTING, .gitignore, facilitator guide, participant handout, environment setup, timeline, build tracker
4. **Set up branch protection** (require PR reviews on main)
5. **Initial commit and push**

### 2.4 Verify
Check the repo URL in your browser. Confirm the structure matches your briefing.

## Phase 3: Content Build — Unblocked Items First (1-2 hours)

### 3.1 Identify what's blocked vs unblocked
Typically, some modules/labs depend on a sandbox codebase that may not be decided yet. Work on what's unblocked first:

**Usually unblocked:**
- Modules focused on prompting, tools intro, governance (no codebase dependency)
- Labs with standalone starter code (not dependent on the sandbox)
- QA framework / review personas
- Facilitator guide details

**Usually blocked on sandbox:**
- Feature-building labs
- Testing labs
- Capstone challenge

### 3.2 Build modules in order
For each module, Claude Code will create:
- `slides/slide-content.md` — Slide-by-slide content notes (convert to Google Slides/Keynote later)
- `exercises/` — In-module exercises with instructions, scenarios, and answer keys
- Updated `README.md` with timing, objectives, and content outline

### 3.3 Build labs in order
For each lab, Claude Code will create:
- `starter/` — Code or materials participants begin with
- `solution/` — Reference solution and answer keys
- `review/` — QA persona checklist specific to that lab

### 3.4 Commit and push after each major piece
Claude Code will commit with descriptive messages and push to the remote.

## Phase 4: QA Framework (30 min)

If your workshop includes a review/quality layer, have Claude Code build:
- **Persona files** — Role-based review prompts (security auditor, edge case hunter, etc.)
- **Templates** — Reusable review workflows (pre-commit, PR review, bug investigation)
- **Examples** — Walkthrough of the review loop with real code

This content is codebase-agnostic and can be built early.

## Phase 5: Codebase Evaluation (when client provides options)

### 5.1 Evaluate client codebases
When the client offers codebases, have Claude Code evaluate each against these criteria:

| Criteria | What to Check |
|---|---|
| **Setup speed** | Can 50 people get it running in under 10 min? No Docker/DB requirements? |
| **Size** | 20-50 Python files is ideal. Too few = not enough to work with. Too many = overwhelming. |
| **Test infrastructure** | Does it have existing pytest tests? Can participants add meaningful tests? |
| **Feature-buildability** | Are there clear extension points for a 30-min feature task? |
| **Dependencies** | Simple `pip install` or complex infrastructure? |
| **Code quality** | Readable but with reviewable patterns (not perfect, not terrible)? |
| **Domain relevance** | Does the domain connect to the audience? |

### 5.2 Make a recommendation
Provide a clear rating (1-10) for each candidate with specific reasoning. Recommend one with a ready-to-send message for the client.

## Phase 6: Sandbox Integration (once codebase is confirmed)

### 6.1 Adapt the codebase
- Copy or reference the chosen codebase into `sandbox/`
- Mock any external API calls for workshop use
- Write tiered tasks (base/intermediate/stretch)
- Create feature specs for labs

### 6.2 Build blocked content
Now build the remaining modules, labs, and capstone that depend on the sandbox.

### 6.3 End-to-end test
- Clone the repo fresh on a clean machine
- Follow the environment setup guide
- Run through every lab from participant perspective
- Verify all solutions work

## Phase 7: Final Polish (week before delivery)

- [ ] Update build tracker with final status
- [ ] Run GA compliance checklist
- [ ] Full dry run with timing
- [ ] Update facilitator guide with real timing from dry run
- [ ] Final grep for tool references that shouldn't be there (e.g., GPT, OpenAI, LangChain)
- [ ] Test fresh clone + setup one more time

---

## Tips for Working with Claude Code

### Do
- **Provide a detailed briefing upfront.** The more context you give (audience, tools, constraints, what to carry over, what to exclude), the better the output.
- **Work in order.** Build infrastructure first, then content, then polish.
- **Build unblocked items first.** Don't wait for all decisions to start producing.
- **Evaluate codebases rigorously.** Setup complexity is the #1 killer in workshops. If it can't be `pip install && pytest` in 5 minutes, it's probably too complex.
- **Commit frequently.** Small commits with clear messages make it easy for the team to review.

### Don't
- **Don't paste tokens or secrets into the chat.** GitHub's secret scanning will revoke them instantly.
- **Don't skip the QA framework.** It differentiates your workshop from a tool demo.
- **Don't build the sandbox before the codebase is confirmed.** It's a moderate rework if you have to swap.
- **Don't assume the source repo maps 1:1.** Adapt structure and content — don't just copy files.

### Claude Code commands used in this build
| Command | What it does |
|---|---|
| `gh auth login` | Authenticate GitHub CLI |
| `gh repo create` | Create new repo on GitHub/GHE |
| `gh api` | Set branch protection rules |
| `git init/add/commit/push` | Standard git operations |
| File read/write/edit | Create and modify all content files |
| `git clone` | Clone source repos for reference |

---

## Checklist: Workshop Repo Completeness

Before handing off to the team:

### Infrastructure
- [ ] Repo created on correct org (GHE)
- [ ] Branch protection enabled (1 reviewer required)
- [ ] README with overview, setup, timeline
- [ ] CONTRIBUTING with team conventions
- [ ] .gitignore for the target language

### Docs
- [ ] Facilitator guide with timing and talking points
- [ ] Participant handout
- [ ] Environment setup instructions
- [ ] Build tracker (what's done, in progress, who owns what)
- [ ] Development timeline

### Content
- [ ] All module READMEs with objectives and content outlines
- [ ] Slide content for completed modules
- [ ] Exercises for completed modules
- [ ] Lab READMEs with tiered instructions
- [ ] Starter code for completed labs
- [ ] Solutions and answer keys
- [ ] Review checklists per lab

### QA Framework (if applicable)
- [ ] Persona files with prompts and checklists
- [ ] Review templates
- [ ] Example walkthrough
- [ ] Common catches reference

### Brand
- [ ] GA compliance checklist in repo
- [ ] No unauthorized tool references in participant-facing materials

---

*This SOP was developed during the NYPL AI-Assisted Software Engineering Workshop build (Feb 2026). Adapt as needed for your workshop's specific requirements.*
