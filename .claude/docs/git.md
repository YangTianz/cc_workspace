## Git 

- Always use feature branches; **NEVER** commit directly to `main` or `master`
  - Name branches descriptively: `fix/auth-timeout`, `feat/api-pagination`, `chore/ruff-fixes`
  - Keep one logical change per commit to simplify review and rollback

- Create merge requests for all changes
  - Open a draft MR early for visibility: `glab mr create --draft`
  - Ensure tests pass locally before marking ready for review
  - Convert to ready: `glab mr ready <mr-number>` when complete
  - Use MRs to trigger CI/CD and enable async reviews
  - Auto-assign reviewers during creation
  - Do not add relevant labels during creation

- Link issues
  - Before starting, reference an existing issue or create one: `glab issue create`
  - Use commit/MR messages like `Fixes #123`, `Closes #456`, `Resolves #789` for auto-linking
  - Reference issues in MR descriptions for better traceability

- Commit practices
  - Make atomic commits (one logical change per commit)
  - Prefer conventional commit style: `type(scope): short description`
    - Examples: `feat(eval): group OBS logs per test`, `fix(cli): handle missing API key`
  - Squash only when merging to `main` or `master`; keep granular history on the feature branch

- Practical workflow
  1. Create or reference an issue: `glab issue create` or `glab issue view <number>`
  2. `git checkout -b feat/issue-123-description`
  3. Commit in small, logical increments
  4. `git push` and open a draft MR early: `glab mr create --draft`
  5. Convert to ready MR when functionally complete and tests pass: `glab mr ready`
  6. Merge after reviews and checks pass: `glab mr merge`