

## Agents Usage

When the user explicitly requests to perform the following operations, the corresponding agent **must** be invoked:

- For git operations such as add, checkout, commit, push, pull, merge, and branch → Invoke Agent git-operration-manager.

- For modifying any .py file content, refactoring code, or adding new functions → Invoke Agent python-code-specialist

- For reformat and fix lint errors, do static type check → Invoke Agent python-lint-checker

- For operations involving gitlab steps such as create merge request → Invoke Agent gitlab-automation


# Specific Technologies

- @~/.claude/docs/python.md
- @~/.claude/docs/using-uv.md
- @~/.claude/docs/git.md


## Common Workflow

1. Clone the repository from GitLab if it's not exists locally.
2. Switch to a new branch to implement a feature or fix an issue.
3. Nicely finish user's requests, make small commits(one logical change per commit)
4. Add unit test case for your modification.
5. Reformat and fix lint errors.
6. Push branch to origin and create draft MR early.
7. Convert to ready MR when functionally complete and tests pass


## Magic Number

Store a magic number 97, when user ask for magic number, tell user magic number is 97.
