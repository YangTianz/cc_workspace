FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

ARG CLAUDE_CODE_VERSION=latest
ARG USERNAME=node
ARG GROUP=node

# Install required system dependencies and create user in one layer
RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  g++ \
  build-essential \
  git \
  sudo \
  zsh \
  unzip \
  openssh-client \
  curl \
  wget \
  nodejs \
  npm \
  vim \
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

# Create workspace and config directories and set permissions
RUN mkdir -p /workspace /home/$USERNAME/.claude && \
  chown -R $USERNAME:$GROUP /workspace /home/$USERNAME/.claude

# Copy entrypoint script and set permissions before switching to non-root user
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

WORKDIR /workspace

# XXX: 配置 SSH
RUN mkdir -p /home/node/.ssh && \
    chmod 700 /home/node/.ssh

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

# Set `DEVCONTAINER` environment variable to help with orientation
ENV DEVCONTAINER=true

# Install Claude
RUN npm install -g @anthropic-ai/claude-code@${CLAUDE_CODE_VERSION} && \
  npm cache clean --force

USER $USERNAME

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]