ARG PROJECT_NAME="{{ project_name }}"

# STAGE 1: BUILD NODE
FROM node:26.4-alpine@sha256:725aeba2364a9b16beae49e180d83bd597dbd0b15c47f1f28875c290bfd255b9 AS build-node
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
FROM python:3.14@sha256:09b29c360b84742bf98eba40b214f7f6b4b53286bb2c8a8b5b1afa188a8d9c0e AS build-python
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.11.26@sha256:3d868e555f8f1dbc324afa005066cd11e1053fc4743b9808ca8025283e65efa5 /uv /uvx /bin/
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
