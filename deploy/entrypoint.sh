#!/bin/bash

# 如果提供了 Git 配置环境变量，则设置 Git 用户信息
if [ ! -z "$GIT_USER_NAME" ]; then
    git config --global user.name "$GIT_USER_NAME"
fi

if [ ! -z "$GIT_USER_EMAIL" ]; then
    git config --global user.email "$GIT_USER_EMAIL"
fi

hostname=$(echo $GITLAB_HOST | sed 's|^http://||' | sed 's|^https://||')
glab auth login --hostname $hostname --token $GITLAB_TOKEN --api-host $hostname --api-protocol http --git-protocol ssh

# 执行CMD命令，保持容器运行
exec "$@"
