# Copyright 2025-2026, Wissem Chiha
#
# Distributed under the LGPL-2.1 license
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1


from __future__ import annotations

import argparse
import sys
from pathlib import Path


def read_directory_owners(path: Path) -> list[str]:
    owners = []
    for line in path.read_text(encoding="utf-8").splitlines():
        owner = line.strip()
        if owner and owner not in owners:
            owners.append(owner)
    return owners


def generated_content(root: Path) -> str:
    owners = []
    owners_files = sorted(
        path
        for path in root.rglob("OWNERS")
        if path != root / "OWNERS" and ".git" not in path.relative_to(root).parts
    )

    for owners_file in owners_files:
        for owner in read_directory_owners(owners_file):
            if owner not in owners:
                owners.append(owner)

    return "\n".join(owners) + ("\n" if owners else "")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if the root OWNERS file does not match the generated content",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    owners_path = root / "OWNERS"
    try:
        current = owners_path.read_text(encoding="utf-8")
        expected = generated_content(root)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1

    if args.check:
        if current != expected:
            print("Root OWNERS is out of date; run amalgamate-owners.py.", file=sys.stderr)
            return 1
        print("Root OWNERS is up to date.")
        return 0

    owners_path.write_text(expected, encoding="utf-8", newline="\n")
    print(f"Updated {owners_path.relative_to(root)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
