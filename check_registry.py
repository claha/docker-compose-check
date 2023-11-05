#!/usr/bin/env python
"""Checking docker compose files to ensure that all images have a defined registry.

Users can customize the list of allowed registries.
"""
import argparse
import sys

DEFAULT_ALLOWED_REGISTRIES = [
    "docker.io",
    "ghcr.io",
    "lscr.io",
    "quay.io",
]


def check_registry(line, allowed_registries):
    """Check if the given line from a Docker Compose file contains a valid image registry."""
    if "image:" not in line:
        return True
    image = line.split("image:")[1].strip()
    if "/" not in image:
        return False
    registry = image.split("/")[0]
    return registry in allowed_registries


def main():
    """Parse arguments, read and validate Docker Compose files based on the provided or default registry order."""
    parser = argparse.ArgumentParser(
        description="Check Docker Compose for registry in image declarations.",
    )
    parser.add_argument("files", nargs="+", help="Docker Compose files to check.")
    parser.add_argument(
        "--allowed_registries",
        default=DEFAULT_ALLOWED_REGISTRIES,
        type=lambda s: s.split(","),
        help="Comma-separated list of allowed image registries.",
    )

    args = parser.parse_args()

    for docker_compose_file in args.files:
        with open(docker_compose_file) as file:
            for line in file.readlines():
                if not check_registry(line, args.allowed_registries):
                    print(
                        f"Invalid registry for '{line.strip()}' in {docker_compose_file}",
                    )
                    sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
