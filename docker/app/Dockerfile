ARG PROJECT_NAME="{{ project_name }}"

# STAGE 1: BUILD NODE
FROM node:26.5-alpine@sha256:e88a35be04478413b7c71c455cd9865de9b9360e1f43456be5951032d7ac1a66 AS build-node
ARG PROJECT_NAME

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
FROM python:3.14@sha256:5f1cdbcab9a50594a79502dd73e885456d2a2fc31f1a1fa18484815b37ee9152 AS build-python
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.11.32@sha256:df4cae8f3a96d175e2e5f992e597550000edbe78fdc2594d5cd8de1a217f504c /uv /uvx /bin/
ENV PYTHONPYCACHEPREFIX=/tmp/pycache
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 \
  PATH=/app/.venv/bin:${PATH}

ARG PROJECT_NAME
ENV DJANGO_SETTINGS_MODULE=${PROJECT_NAME}.settings


RUN --mount=type=cache,target=/root/.cache/uv \
  --mount=type=bind,source=uv.lock,target=uv.lock \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  uv sync --locked

COPY . ./
COPY --from=build-node /app/dist/ /opt/static/

# Copy JS vendor libs to be included globally in Django
ARG VENDOR_PATH=/opt/static/vendor
ARG MODULES_PATH=/app/node_modules

RUN mkdir -p ${VENDOR_PATH}
# Copy Alpine.js (CSP-compatible build):
COPY --from=build-node ${MODULES_PATH}/@alpinejs/csp/dist/cdn.js ${VENDOR_PATH}/alpine.js
COPY --from=build-node ${MODULES_PATH}/@alpinejs/csp/dist/cdn.min.js ${VENDOR_PATH}/alpine.min.js
# Copy HTMX:
COPY --from=build-node ${MODULES_PATH}/htmx.org/dist/htmx.js ${VENDOR_PATH}/htmx.js
COPY --from=build-node ${MODULES_PATH}/htmx.org/dist/htmx.min.js ${VENDOR_PATH}/htmx.min.js

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

CMD ["gunicorn", "$PROJECT_NAME.wsgi"]
