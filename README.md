# Overview

Tiny test flask app used to verify that docker environment variables and secrets are correctly hooked up.

## Use case

Useful for debugging AWS ECS access issues.

## Docker hub

Built images are pushed to https://hub.docker.com/r/rocketnovadockerhub/tiny-env-test/tags

0. `docker login -u rocketnovadockerhub`
1. `cd app`
2. `make release-build`
3. `docker tag <tag> rocketnovadockerhub/tiny-env-test:latest`
4. `docker push rocketnovadockerhub/tiny-env-test:latest`
