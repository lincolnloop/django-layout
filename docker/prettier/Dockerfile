FROM node:26.2-alpine@sha256:7c6af15abe4e3de859690e7db171d0d711bf37d27528eddfe625b2fe89e097f8 AS ui

WORKDIR /root
RUN --mount=type=bind,source=docker/prettier/package.json,target=package.json \
    --mount=type=bind,source=docker/prettier/package-lock.json,target=package-lock.json \
    npm install --no-save

WORKDIR /root/app
