# --- Dockerfile ---

# Start from the current Debian stable "slim" image. It's smaller than the full
# image but contains all the necessary basics like a package manager.
FROM debian:stable-slim

# Set environment variables.
# - DEBIAN_FRONTEND=noninteractive: Prevents `apt-get` from asking interactive questions.
# - PATH: Prepend the user's local bin directory to the PATH. This is where we will install our tools.
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/home/developer/.local/bin:${PATH}"

# Install the absolute minimal system dependencies required for our bootstrap.
# - curl: To download the installers.
# - unzip: The `uv` installer script uses it.
# - ca-certificates: To allow `curl` to verify HTTPS certificates.
# We run update, install, and cleanup in a single RUN layer to keep the image size small.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        unzip \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user for good security practice. A real user wouldn't work as root.
# -m: Create the user's home directory.
# -s: Set the default shell for the user.
RUN useradd --create-home --shell /bin/bash developer

# Switch to our newly created user. Subsequent commands will run as `developer`.
USER developer
WORKDIR /home/developer

# --- This is the "Zero to Hero" Bootstrap, exactly as you designed it ---

# 1. Install 'just' into the user's local bin.
#    The --to flag is used to specify the install location.
RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /home/developer/.local/bin

# 2. Install 'uv' into the user's home directory (its default location).
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# --- Project Setup ---

# Copy the project files from your local machine into the container's working directory.
# We use --chown to ensure the files are owned by our `developer` user, not root.
COPY --chown=developer:developer justfile README.md ./

# this will install all Python virtualenvs as a side-effect and make them part of the image itself
RUN just version-all

# Set the default command to run when someone starts the container.
# Running `just` without arguments lists all available recipes, which is the perfect
# self-documenting entry point for anyone exploring the container.
# CMD ["just"]
# CMD just && just version-all
CMD ["/usr/bin/bash", "-c", "echo && just && echo && just version-all"]
