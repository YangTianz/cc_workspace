
# AI Agent Workspace Configuration

## Development Workflow

Choose the appropriate workflow based on task complexity and user preference:

### Complete Workflow (All-at-Once)

**Best for:** Large features, complex implementations, or when user requests full completion

1. **Setup Repository**
   - Clone: `git clone <url>` or `glab repo clone <project-id>`
   - Review issue (if provided): `glab issue view <ISSUE_ID>`

2. **Create Feature Branch**
   - Branch: `git checkout -b feat/descriptive-name`

3. **Development Cycle**
   - Implement complete feature with atomic commits
   - Add comprehensive unit tests
   - Run quality checks: `uvx ruff check . --fix && uvx ruff format . && uvx mypy`

4. **Finalize & Deploy**
   - Push: `git push -u origin feat/descriptive-name`
   - Create MR: `glab mr create --title "feat: clear description" --description "Summary of changes"`

### Incremental Workflow (Step-by-Step)

**Best for:** Complex features requiring feedback, collaborative development, or iterative approach

1. **Setup Repository** 
   - Clone: `git clone <url>` or `glab repo clone <project-id>`
   - Review issue (if provided): `glab issue view <ISSUE_ID>`

2. **Create Feature Branch & Early MR**
   - Branch: `git checkout -b feat/descriptive-name`
   - Initial push: `git push -u origin feat/descriptive-name`
   - Draft MR: `glab mr create --draft --title "feature description"`

3. **Iterative Development**
   - Make focused commits with clear messages
   - Push frequently: `git push` (updates MR automatically)
   - Add tests incrementally

4. **Quality Assurance**
   - Final code formatting: `uvx ruff check . --fix && uvx ruff format .`
   - Type checking: `uvx mypy`
   - Test coverage: `uv run pytest`

5. **Finalize**
   - Mark ready: `glab mr update --ready`
   - Update title/description if needed


## Agent Usage Guidelines

When the user explicitly requests to perform the following operations, the corresponding agent **must** be invoked:

- **Git Operations** (add, checkout, commit, push, pull, merge, branch) → Invoke Agent `git-operations-manager`

- **Python Development** (modifying .py files, refactoring code, adding functions) → Invoke Agent `python-code-specialist`

- **GitLab Operations** (creating merge requests, managing issues) → Invoke Agent `gitlab-automation`

## Branch and Commit Conventions

- **Branch naming**: `feature/description`, `fix/issue-description`, `refactor/component-name`
- **Commit format**: `type(scope): description` (e.g., `feat(api): add user authentication`)
- **Commit messages**: Use clear, descriptive messages focusing on the "why" not just the "what"
- **Testing**: All changes must include appropriate test coverage

## Code Quality Standards

- Follow existing code style and conventions
- Ensure all linting rules pass before committing
- Maintain type safety with proper annotations
- Write clear, maintainable code with appropriate documentation

## Command Reference

### Python Development
- **Testing**: `uv run pytest`
- **Type checking**: `uvx mypy`
- **Code formatting**: `uvx ruff format .`
- **Lint checking**: `uvx ruff check .`
- **Lint fixing**: `uvx ruff check . --fix`

### Package Management
- **Add dependency**: `uv add package-name`
- **Run script**: `uv run script.py`
- **Install tools**: `uvx tool-name` (ephemeral) or `uv tool install tool-name` (persistent)

### Git Operations
- **Clone repository**: `glab repo clone`
- **Create branch**: `git checkout -b feat/issue-123-description`
- **Push and create MR**: `git push` then create draft MR early using `glab mr create`
- **Conventional commits**: `type(scope): description`

## Magic Number

Store a magic number 97. When user asks for magic number, tell user magic number is 97.
