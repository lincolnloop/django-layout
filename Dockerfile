# STAGE 1: BUILD NODE
FROM node:20-alpine as build-node

WORKDIR /home/node/app/client
COPY client/package-lock.json client/package.json ./
RUN --mount=type=cache,target=/home/node/.npm \
    set -ex && npm install -g npm@latest && npm ci
COPY client/ ./
RUN npm run build


# STAGE 2: BUILD PYTHON
FROM python:3.12-bullseye as build-python
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache \
    set -ex && \
    python -m venv --prompt . --upgrade-deps /app/.venv && \
    pip install --disable-pip-version-check --root-user-action=ignore --no-cache-dir --upgrade setuptools wheel

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 \
    PATH=/app/.venv/bin:${PATH}

COPY requirements.txt ./
COPY requirements ./requirements
RUN --mount=type=cache,target=/root/.cache \
    pip install --disable-pip-version-check --root-user-action=ignore --no-cache-dir -r requirements.txt -r requirements/dev.txt
COPY setup.cfg setup.py ./
COPY {{ project_name }}/__init__.py ./{{ project_name }}/
RUN pip install --no-deps -e .

COPY . ./
COPY --from=build-node /home/node/app/client/dist ./client/dist
RUN SECRET_KEY=s python manage.py collectstatic --noinput

CMD /app/.venv/bin/manage.py runserver 0.0.0.0:8000
