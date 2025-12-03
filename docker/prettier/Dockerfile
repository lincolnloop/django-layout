FROM node:25.2-alpine AS ui

WORKDIR /root
RUN --mount=type=bind,source=docker/prettier/package.json,target=package.json \
    --mount=type=bind,source=docker/prettier/package-lock.json,target=package-lock.json \
    npm install --no-save

WORKDIR /root/app
