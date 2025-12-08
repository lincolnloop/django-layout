# STAGE 1: BUILD NODE
FROM node:25.2.1-alpine AS build-node

WORKDIR /home/node/app/client
COPY client/package-lock.json client/package.json ./
RUN --mount=type=cache,target=/home/node/.npm \
  set -ex && npm install -g npm@latest && npm ci
COPY client/ ./
RUN npm run build


# STAGE 2: BUILD PYTHON
FROM python:3.14 AS build-python
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.9.16 /uv /uvx /bin/
ENV PYTHONPYCACHEPREFIX=/tmp/pycache
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 \
  PATH=/app/.venv/bin:${PATH}


RUN --mount=type=cache,target=/root/.cache/uv \
  --mount=type=bind,source=uv.lock,target=uv.lock \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  uv sync --locked

COPY . ./
COPY --from=build-node /home/node/app/client/dist ./client/dist
RUN SECRET_KEY=s python manage.py collectstatic --noinput

EXPOSE 8000
ENV PORT=8000
# assumes the server is running behind a reverse proxy (Nginx, AWS ALB, etc.)
# set the `WEB_CONCURRENCY` environment variable to the number of workers you'd
# like to run
ENV GUNICORN_CMD_ARGS="\
  --access-logfile=- \
  --bind=0.0.0.0:$PORT \
  --forwarded-allow-ips '*' \
  --timeout=10 \
  "

CMD ["gunicorn", "{{ project_name }}.wsgi:application"]
