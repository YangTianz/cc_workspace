
# AI Agent Workspace Configuration

## Agent Usage Guidelines

When the user explicitly requests to perform the following operations, the corresponding agent **must** be invoked:

- **Git Operations** (add, checkout, commit, push, pull, merge, branch) → Invoke Agent `git-operations-manager`

- **Python Development** (modifying .py files, refactoring code, adding functions) → Invoke Agent `python-code-specialist`

- **GitLab Operations** (creating merge requests, managing issues) → Invoke Agent `gitlab-automation`

## Development Workflow

1. Clone the repository from GitLab if it doesn't exist locally.
2. Switch to a new feature branch to implement changes or fix issues.
3. Complete user requests with focused, small commits (one logical change per commit).
4. Add comprehensive unit test cases for modifications.
5. Reformat code and fix lint errors using appropriate tools.
6. Push branch to origin and create draft MR early for visibility.
7. Convert to ready MR when functionally complete and all tests pass.

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
