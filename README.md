# Docker Compose Check

A set of pre-commit hooks to check docker compose files.

First, ensure you have `pre-commit` installed. Follow the
[official installation guide](https://pre-commit.com/#install) for instructions.

## Registry check

A pre-commit hook that ensures all images in docker compose files have a defined
registry. Valid filenames are `docker-compose.yaml` and `compose.yaml`, including
the shorter extension `.yml`. Also supports jinja2 templates, i.e. a second extension
`.j2` after the previously mentioned filenames.

## Socket check

A pre-coomit hook that ensures all bind mounts of the docker.sock is read-only.

## No new privileges check

A pre-coomit hook that ensures all docker compose files set no-new-privileges to
true.

## Configuration

Create a `.pre-commit-config.yaml` in your repository (if it doesn't already exist)
and add this repository to it:

```yaml
repos:
  - repo: https://github.com/claha/docker-compose-check
    rev: v0.2.0  # Use the ref you want
    hooks:
      - id: check-registry
        args: ['--allowed_registries=docker.io,quay.io,my.custom.registry']  # Optional
      - id: check-socket
      - id: check-no-new-privileges
```
