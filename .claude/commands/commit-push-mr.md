---
allowed-tools: Bash(git checkout --branch:*), Bash(git add:*), Bash(git status:*), Bash(git push:*), Bash(git commit:*)
description: Commit, push, and open a MR
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`

## Your task

Based on the above changes:
1. Create a new branch if on main/master
2. Create a single commit with an appropriate message
3. Push the branch to origin, add `-o merge_request.create` to create a merge request, add `merge_request.title="<title>"` to set the MR's title and add `-o merge_request.description="<description>"` to set descripiton.
4. You have the capability to call multiple tools in a single response. You MUST do all of the above in a single message. Do not use any other tools or do anything else. Do not send any other text or messages besides these tool calls.
