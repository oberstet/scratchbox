# Using Docker with just

https://hynek.me/articles/docker-uv/

## Build the image

```
oberstet@amd-ryzen5:~/scm/oberstet/sempervivum/dockerized$ just docker-build
==> Building Docker image 'just-demo'...
docker build -t just-demo .
[+] Building 25.8s (12/12) FINISHED                                                                             docker:default
 => [internal] load build definition from Dockerfile                                                                      0.0s
 => => transferring dockerfile: 2.29kB                                                                                    0.0s
 => [internal] load metadata for docker.io/library/debian:stable-slim                                                     1.8s
 => [internal] load .dockerignore                                                                                         0.0s
 => => transferring context: 2B                                                                                           0.0s
 => [1/7] FROM docker.io/library/debian:stable-slim@sha256:7e0b7fe7c6d695d615eabaea8d19adf592a6a9ff3dbd5206d3e31139b9afd  5.0s
 => => resolve docker.io/library/debian:stable-slim@sha256:7e0b7fe7c6d695d615eabaea8d19adf592a6a9ff3dbd5206d3e31139b9afd  0.0s
 => => sha256:4903f7352a46e5fb3b3920584385ef74541d936d7f9e6a86859f0691e14c375b 28.23MB / 28.23MB                          3.1s
 => => sha256:7e0b7fe7c6d695d615eabaea8d19adf592a6a9ff3dbd5206d3e31139b9afdfa7 8.54kB / 8.54kB                            0.0s
 => => sha256:f50a722f83a90d32a41848c288e2a2e35d6eaa0b56268ef69bf47245d7f70683 1.02kB / 1.02kB                            0.0s
 => => sha256:79f87d48cf6e2c35ab97516e4fc2098ffae34909509a0e43873c8dfe4cdbfc7d 451B / 451B                                0.0s
 => => extracting sha256:4903f7352a46e5fb3b3920584385ef74541d936d7f9e6a86859f0691e14c375b                                 1.7s
 => [internal] load build context                                                                                         0.0s
 => => transferring context: 2.18kB                                                                                       0.0s
 => [2/7] RUN apt-get update &&     apt-get install -y --no-install-recommends         curl         unzip         ca-ce  10.1s
 => [3/7] RUN useradd --create-home --shell /bin/bash developer                                                           0.3s
 => [4/7] WORKDIR /home/developer                                                                                         0.1s
 => [5/7] RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /home/developer/.lo  3.6s
 => [6/7] RUN curl -LsSf https://astral.sh/uv/install.sh | sh                                                             4.6s
 => [7/7] COPY --chown=developer:developer justfile README.md ./                                                          0.1s
 => exporting to image                                                                                                    0.2s
 => => exporting layers                                                                                                   0.2s
 => => writing image sha256:a1d553473db762abe26387cda24e8b84a9e86e90bebe1046ec0675f2f1b45735                              0.0s
 => => naming to docker.io/library/just-demo                                                                              0.0s
```

## List recipes locally

```
oberstet@amd-ryzen5:~/scm/oberstet/sempervivum/dockerized$ just
Available recipes:
    default           # list all recipes
    docker-build      # Build the Docker image from the Dockerfile in the current directory.
    docker-exec +args # Usage: just docker-exec hello_final 5
    docker-run        # Run the container with its default command (`just --list`).
    venv env          # Usage: `just venv cpy312`
    version env       # Usage: `just version cpy312`
    version-all       # It uses a shell loop, which is simple and obvious.
```

## List recipes from within container

```
oberstet@amd-ryzen5:~/scm/oberstet/sempervivum/dockerized$ just docker-run
==> Running container with default command...
docker run --rm -it just-demo
Available recipes:
    default           # list all recipes
    docker-build      # Build the Docker image from the Dockerfile in the current directory.
    docker-exec +args # Usage: just docker-exec hello_final 5
    docker-run        # Run the container with its default command (`just --list`).
    venv env          # Usage: `just venv cpy312`
    version env       # Usage: `just version cpy312`
    version-all       # It uses a shell loop, which is simple and obvious.
oberstet@amd-ryzen5:~/scm/oberstet/sempervivum/dockerized$
```
