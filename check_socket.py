#!/usr/bin/env python
"""Checking docker compose files to ensure that all bind mounts of docker.sock is read-only."""

import argparse
import sys


def check_socket(line):
    """Check if the given line from a Docker Compose file contains a valid bind mount."""
    if "docker.sock" not in line:
        return True
    return line.strip().endswith(":ro")


def main():
    """Parse arguments, read and validate Docker Compose files."""
    parser = argparse.ArgumentParser(
        description="Check Docker Compose bind mount of docker.sock.",
    )
    parser.add_argument("files", nargs="+", help="Docker Compose files to check.")

    args = parser.parse_args()

    for docker_compose_file in args.files:
        with open(docker_compose_file) as file:
            for line in file.readlines():
                if not check_socket(line):
                    print(
                        f"Docker socket is not read-only (ro) in {docker_compose_file}",
                    )
                    sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
