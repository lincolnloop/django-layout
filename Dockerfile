# STAGE 1: BUILD NODE
FROM node:20-alpine AS build-node

WORKDIR /home/node/app/client
COPY client/package-lock.json client/package.json ./
RUN --mount=type=cache,target=/home/node/.npm \
    set -ex && npm install -g npm@latest && npm ci
COPY client/ ./
RUN npm run build


# STAGE 2: BUILD PYTHON
FROM python:3.12-bullseye AS build-python
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache \
    set -ex && \
    python -m venv --prompt . --upgrade-deps /app/.venv && \
    /app/.venv/bin/pip install --disable-pip-version-check --root-user-action=ignore --no-cache-dir --upgrade setuptools wheel

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 \
    PATH=/app/.venv/bin:${PATH}

ARG PY_REQUIREMENTS_FILE=requirements.txt
COPY requirements.txt requirements-dev.txt ./
RUN --mount=type=cache,target=/root/.cache \
    pip install --disable-pip-version-check --root-user-action=ignore --no-cache-dir -r "$PY_REQUIREMENTS_FILE"

COPY . ./
COPY --from=build-node /home/node/app/client/dist ./client/dist
RUN SECRET_KEY=s python manage.py collectstatic --noinput

EXPOSE 8000
ENV PORT=8000
# assumes the server is running behind a reverse proxy (Nginx, AWS ALB, etc.)
# set the `WEB_CONCURRENCY` environment variable to the number of workers you'd like to run
CMD gunicorn --access-logfile=- --timeout=10 --bind=0.0.0.0:$PORT --forwarded-allow-ips '*' {{ project_name }}.wsgi:application
