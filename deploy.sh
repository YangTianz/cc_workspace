#!/bin/bash

# 停止并删除旧容器
docker stop ytz-ai-agent || true
docker rm ytz-ai-agent || true

# 重新构建镜像
docker build -t ytz-ai-agent-image .

# 使用 .env 文件启动新容器
docker run -d --name ytz-ai-agent --env-file .env -v ~/.ssh/id_rsa:/home/node/.ssh/id_rsa ytz-ai-agent-image

echo "容器 ytz-ai-agent 已成功更新并启动"
