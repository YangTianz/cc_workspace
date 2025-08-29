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
  jq \
  && groupadd --gid 1000 $GROUP \
  && useradd --uid 1000 --gid $GROUP --shell /bin/bash --create-home $USERNAME \
  && mkdir -p /usr/local/share/npm-global \
  && chown -R $USERNAME:$GROUP /usr/local/share \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /tmp/* /var/tmp/* \
  && curl -sSL "https://raw.githubusercontent.com/upciti/wakemeops/main/assets/install_repository" | sudo bash \
  && sudo apt install glab

# Persist bash history.
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  && mkdir /commandhistory \
  && touch /commandhistory/.bash_history \
  && chown -R $USERNAME /commandhistory

# Create workspace and config directories and set permissions
RUN mkdir -p /workspace /home/$USERNAME/.claude && \
  chown -R $USERNAME:$GROUP /workspace /home/$USERNAME/.claude

# Copy entrypoint script and set permissions before switching to non-root user
COPY deploy/entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY .claude/ /home/$USERNAME/.claude/
COPY claude_agent.py /home/$USERNAME/claude_agent.py

RUN mkdir -p /home/node/.ssh && \
    chmod 700 /home/node/.ssh

# Set up non-root user
USER $USERNAME

# Install global packages and set environment variables
ENV NPM_CONFIG_PREFIX=/usr/local/share/npm-global \
    PATH=$PATH:/usr/local/share/npm-global/bin \
    SHELL=/bin/zsh \
    EDITOR=vim \
    VISUAL=vim \
    DEVCONTAINER=true

# Install Claude
RUN npm install -g @anthropic-ai/claude-code@${CLAUDE_CODE_VERSION} && \
  npm cache clean --force

USER $USERNAME
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

WORKDIR /home/$USERNAME
CMD ["uv", "run", "--script", "claude_agent.py"]
