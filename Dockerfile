FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

ARG CLAUDE_CODE_VERSION=latest
ARG USERNAME=node
ARG GROUP=node

# Install required system dependencies and create user in one layer
RUN apt-get update && apt-get install -y --no-install-recommends \
  git \
  sudo \
  zsh \
  unzip \
  openssh-client \
  curl \
  nodejs \
  npm \
  && groupadd --gid 1000 $GROUP \
  && useradd --uid 1000 --gid $GROUP --shell /bin/bash --create-home $USERNAME \
  && mkdir -p /usr/local/share/npm-global \
  && chown -R $USERNAME:$GROUP /usr/local/share \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /tmp/* /var/tmp/*

# Persist bash history.
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  && mkdir /commandhistory \
  && touch /commandhistory/.bash_history \
  && chown -R $USERNAME /commandhistory

# Set `DEVCONTAINER` environment variable to help with orientation
ENV DEVCONTAINER=true

# Create workspace and config directories and set permissions
RUN mkdir -p /workspace /home/$USERNAME/.claude && \
  chown -R $USERNAME:$GROUP /workspace /home/$USERNAME/.claude

WORKDIR /workspace

# # 配置 git 用户信息
# RUN git config --global user.name "${GIT_USER_NAME}" && \
#     git config --global user.email "${GIT_USER_EMAIL}"

# XXX: 配置 SSH
RUN mkdir -p /home/node/.ssh && \
    chmod 700 /home/node/.ssh && \
    chown -R $USERNAME:$GROUP /home/$USERNAME/.ssh

# Set up non-root user
USER $USERNAME

# Install global packages
ENV NPM_CONFIG_PREFIX=/usr/local/share/npm-global
ENV PATH=$PATH:/usr/local/share/npm-global/bin

# Set the default shell to zsh rather than sh
ENV SHELL=/bin/zsh

# Set the default editor and visual
ENV EDITOR=vim
ENV VISUAL=vim

# Install Claude
RUN npm install -g @anthropic-ai/claude-code@${CLAUDE_CODE_VERSION} && \
  npm cache clean --force

USER $USERNAME

ENV ANTHROPIC_AUTH_TOKEN=${ANTHROPIC_AUTH_TOKEN}
CMD ["tail", "-f", "/dev/null"] 
