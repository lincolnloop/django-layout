# STAGE 1: BUILD NODE
FROM node:25.2-alpine AS build-node
ARG PROJECT_NAME="{{ project_name }}"

WORKDIR /app
RUN --mount=type=bind,source=package.json,target=package.json \
  --mount=type=bind,source=package-lock.json,target=package-lock.json \
  npm install --no-save

RUN --mount=type=bind,source=package.json,target=package.json \
  --mount=type=bind,source=package-lock.json,target=package-lock.json \
  --mount=type=bind,source=ui/,target=ui/ \
  --mount=type=bind,source=${PROJECT_NAME},target=${PROJECT_NAME}/ \
  npm run tailwind-build



# STAGE 2: BUILD PYTHON
FROM python:3.14 AS build-python
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.9.17 /uv /uvx /bin/
ENV PYTHONPYCACHEPREFIX=/tmp/pycache
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 \
  PATH=/app/.venv/bin:${PATH}

ARG PROJECT_NAME="{{ project_name }}"
ENV DJANGO_SETTINGS_MODULE=${PROJECT_NAME}.settings


RUN --mount=type=cache,target=/root/.cache/uv \
  --mount=type=bind,source=uv.lock,target=uv.lock \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  uv sync --locked

COPY . ./
COPY --from=build-node /app/dist/ /opt/static/
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

CMD ["gunicorn", "{{ project_name }}.wsgi"]
