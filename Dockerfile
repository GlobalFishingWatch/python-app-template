# ---------------------------------------------------------------------------------------
# BASE IMAGE
# ---------------------------------------------------------------------------------------
FROM python:3.12.10-slim AS base

# Configure the working directory
RUN mkdir -p /opt/project
WORKDIR /opt/project

# Setup a volume for configuration and authtentication.
VOLUME ["/root/.config"]

# Update system and install build tools.
RUN apt-get update && apt-get install -y gcc g++ build-essential

# Upgrade PIP
RUN pip install --upgrade pip

# ---------------------------------------------------------------------------------------
# DEPENDENCIES IMAGE (installed project dependencies)
# ---------------------------------------------------------------------------------------
# We do this first so when we modify code while development,
# this layer is reused from cache.
FROM base AS deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------------------------------------------------------------------------------------
# Apache Beam integration IMAGE
# ---------------------------------------------------------------------------------------
FROM deps AS beam
# Copy files from official SDK image, including script/dependencies.
# IMPORTANT: This version must match the one in requirements.txt
COPY --from=apache/beam_python3.12_sdk:2.64.0 /opt/apache/beam /opt/apache/beam

# Set the entrypoint to Apache Beam SDK launcher.
ENTRYPOINT ["/opt/apache/beam/boot"]

# ---------------------------------------------------------------------------------------
# PRODUCTION IMAGE
# ---------------------------------------------------------------------------------------
# If you need Apache Beam integration, replace "deps" base image with "beam".
FROM deps AS prod

COPY . /opt/project
RUN pip install .

# ---------------------------------------------------------------------------------------
# DEVELOPMENT IMAGE (editable install and development tools)
# ---------------------------------------------------------------------------------------
# If you need Apache Beam integration, replace "deps" base image with "beam".
FROM deps AS dev

COPY . /opt/project
RUN pip install -e .[lint,test,dev,build]