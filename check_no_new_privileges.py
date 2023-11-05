#!/usr/bin/env python
"""Checking docker compose files to ensure that no-new-privileges is set to true."""
import argparse
import sys


def check_no_new_privileges(line):
    """Check if the given line from a Docker Compose file sets no-new-privileges to true."""
    return line.strip() == "- no-new-privileges:true"


def main():
    """Parse arguments, read and validate Docker Compose files."""
    parser = argparse.ArgumentParser(
        description="Check Docker Compose no-new-privileges set to true.",
    )
    parser.add_argument("files", nargs="+", help="Docker Compose files to check.")

    args = parser.parse_args()

    for docker_compose_file in args.files:
        no_new_privileges = False
        with open(docker_compose_file) as file:
            for line in file.readlines():
                if check_no_new_privileges(line):
                    no_new_privileges = True
                    break
        if not no_new_privileges:
            print(
                f"Docker Compose did not set no-new-privliges to true in {docker_compose_file}",
            )
            sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
