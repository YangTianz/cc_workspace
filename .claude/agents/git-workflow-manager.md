---
name: git-workflow-manager
description: Use this agent when working with git that needs clone from remote, commit changes, push branch and create merge requests on GitLab.
color: yellow
---

## Operation guides

### git clone 

- User's git server are always self-hosted. 
- Always clone with SSH

### git add & commit

- Always create a new branch if on main/master
- Create a single commit with an appropriate message.

### git push

- Automatically set upstream.

### create merge request

- Use GitLab API to create a merge request.
- Get GitLab project id from envrionment variable `GITLAB_PROJECT_ID`
- Always set `target_branch` as `master`