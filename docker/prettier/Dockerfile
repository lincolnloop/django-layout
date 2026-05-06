FROM node:25.9-alpine@sha256:bdf2cca6fe3dabd014ea60163eca3f0f7015fbd5c7ee1b0e9ccb4ced6eb02ef4 AS ui

WORKDIR /root
RUN --mount=type=bind,source=docker/prettier/package.json,target=package.json \
    --mount=type=bind,source=docker/prettier/package-lock.json,target=package-lock.json \
    npm install --no-save

WORKDIR /root/app
