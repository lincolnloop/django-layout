ARG PROJECT_NAME="{{ project_name }}"

# STAGE 1: BUILD NODE
FROM node:26.2-alpine@sha256:7c6af15abe4e3de859690e7db171d0d711bf37d27528eddfe625b2fe89e097f8 AS build-node
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
FROM python:3.14@sha256:6f473f84b09fccf411d4875e19e9e2796b59d6b3c722463d2963384a43e59f39 AS build-python
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.11.21@sha256:ff07b86af50d4d9391d9daf4ff89ce427bc544f9aae87057e69a1cc0aa369946 /uv /uvx /bin/
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
