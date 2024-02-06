# STAGE 1: BUILD NODE
FROM node:18-alpine as build-node

WORKDIR /home/node/app
COPY package-lock.json package.json ./
RUN set -ex && npm install -g npm@latest && npm ci
COPY client/ ./client
RUN set -ex && npm run build && npm test


# STAGE 2: BUILD PYTHON
FROM python:3.9-buster as build-python
RUN mkdir /app && python -m venv /app/.venv && /app/.venv/bin/python -m pip install -U pip wheel setuptools

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 \
    PATH=/app/.venv/bin:${PATH}

WORKDIR /app

COPY requirements.txt ./
COPY requirements ./requirements
RUN pip install -r requirements.txt -r requirements/dev.txt
COPY setup.cfg setup.py ./
COPY {{ project_name }}/__init__.py ./{{ project_name }}/
RUN pip install --no-deps -e .

COPY . ./

CMD /app/.venv/bin/manage.py runserver 0.0.0.0:8000
