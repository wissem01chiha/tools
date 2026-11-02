# Copyright 2025-2026, Wissem Chiha
#
# Distributed under the LGPL-2.1 license
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1

# This script is for internal tooling only, it goal is
# to amalgamate requirements.txt from each subfolder and
# create a global requirements.txt for the one-shot installtion
# of all python dependencies

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def read_directory_requirements(path: Path) -> list[str]:
    requirements = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        print(f"failed to read {path}: {e}", file=sys.stderr)
        raise

    for line in text.splitlines():
        requirement = line.strip()
        if requirement and requirement not in requirements:
            requirements.append(requirement)

    return requirements

def generated_content(root: Path) -> str:
    requirements = []
    requirements_files = sorted(
        path
        for path in root.rglob("requirements.txt")
        if path != root / "requirements.txt" and ".git" not in path.relative_to(root).parts
    )

    for requirements_file in requirements_files:
        for owner in read_directory_requirements(requirements_file):
            if owner not in requirements:
                requirements.append(owner)

    return "\n".join(requirements) + ("\n" if requirements else "")

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if the root requirement.txt file does not match the generated content",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    requirements_path = root / "requirements.txt"
    try:
        current = requirements_path.read_text(encoding="utf-8")
        expected = generated_content(root)
    except UnicodeDecodeError as e:
        print(f"failed to read root requirements file {requirements_path}: {e}",
                file=sys.stderr)
        return 1

    if args.check:
        if current != expected:
            print("requirements.txt is out of date; run amalgamate-requirements.py.", file=sys.stderr)
            return 1
        print("requirements.txt is up to date.")
        return 0

    requirements_path.write_text(expected, encoding="utf-8", newline="\n")
    print(f"updated {requirements_path.relative_to(root)}.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
