#!/bin/bash

# 停止并删除旧容器
docker stop ytz-ai-agent || true
docker rm ytz-ai-agent || true

# # 删除旧镜像
# docker rmi ytz-ai-agent-image || true

# 重新构建镜像
docker build -t ytz-ai-agent-image .

# 使用 .env 文件启动新容器
docker run -d --name ytz-ai-agent \
    --network host \
    --env-file .env \
    -v ~/.ssh:/home/node/.ssh:ro \
    -v ~/monorepo:/workspace/monorepo \
    ytz-ai-agent-image

echo "容器 ytz-ai-agent 已成功更新并启动"
