FROM node:20-alpine

RUN apk add --no-cache less git sudo zsh unzip python3 curl openssh-client && \
  mkdir -p /usr/local/share/npm-global && \
  chown -R node:node /usr/local/share

ARG USERNAME=node

# Persist bash history.
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  && mkdir /commandhistory \
  && touch /commandhistory/.bash_history \
  && chown -R $USERNAME /commandhistory

# Set `DEVCONTAINER` environment variable to help with orientation
ENV DEVCONTAINER=true

# Create workspace and config directories and set permissions
RUN mkdir -p /workspace /home/node/.claude && \
  chown -R node:node /workspace /home/node/.claude

WORKDIR /workspace

# # 配置 git 用户信息
# RUN git config --global user.name "${GIT_USER_NAME}" && \
#     git config --global user.email "${GIT_USER_EMAIL}"

# XXX: 配置 SSH
RUN mkdir -p /home/node/.ssh && \
    chmod 700 /home/node/.ssh && \
    chown -R node:node /home/node/.ssh

# Set up non-root user
USER node

# Install global packages
ENV NPM_CONFIG_PREFIX=/usr/local/share/npm-global
ENV PATH=$PATH:/usr/local/share/npm-global/bin

# Set the default shell to zsh rather than sh
ENV SHELL=/bin/zsh

# Install Claude
RUN npm install -g @anthropic-ai/claude-code && \
  npm cache clean --force

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV ANTHROPIC_AUTH_TOKEN=${ANTHROPIC_AUTH_TOKEN}
CMD ["tail", "-f", "/dev/null"]
