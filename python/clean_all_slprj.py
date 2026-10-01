#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clean all 'slprj' folders in a given directory (optionally recursive).

Usage:
  python clean_all_slprj.py --dir D:\ePT_HCP_AutosarMigration-2020b -r
Options:
  --dir / -d       Root directory to inspect.
  -r / --recursive Recurse into all subdirectories.
  --dry-run        Show what would be deleted but don't delete anything.
  --force          Do not prompt for confirmation.
  --verbose        Print extra details.
  --quiet          Minimal output (only errors + final summary).
  --version        Show version and exit.
"""

from __future__ import annotations
import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import List, Tuple

__version__ = "1.0.0"

SLPRJ_NAME = "slprj"


def is_symlink_or_junction(path: Path) -> bool:
    """
    Return True if path is a symlink or a Windows junction.
    pathlib.Path.is_symlink() covers symlinks; for junctions, os.path.islink
    may not detect on older Python/Windows combos, but rmtree with onerror
    will still protect us; we keep this check to avoid following links.
    """
    try:
        return path.is_symlink()
    except OSError:
        return False


def find_slprj_dirs(root: Path, recursive: bool) -> List[Path]:
    """
    Find all directories named 'slprj' under root.
    If recursive=False, only checks direct children of root.
    """
    matches: List[Path] = []

    if not root.exists() or not root.is_dir():
        return matches

    if recursive:
        for current, dirs, _files in os.walk(root):
            cur_path = Path(current)
            safe_dirs = []
            for d in dirs:
                p = cur_path / d
                if is_symlink_or_junction(p):
                    continue
                safe_dirs.append(d)
            dirs[:] = safe_dirs  

            for d in dirs:
                if d.lower() == SLPRJ_NAME:
                    matches.append(cur_path / d)
    else:
        for child in root.iterdir():
            if child.is_dir() and child.name.lower() == SLPRJ_NAME:
                matches.append(child)

    matches = sorted(set(p.resolve() for p in matches))
    return matches


def delete_dir(path: Path, verbose: bool = False) -> Tuple[bool, str]:
    """
    Delete the directory at path. Returns (ok, message).
    """
    try:
        if verbose:
            print(f"[INFO] Deleting: {path}")
        def onerror(func, p, exc_info):
            try:
                os.chmod(p, 0o700)
                func(p)
            except Exception:
                pass 

        shutil.rmtree(path, onerror=onerror)
        return True, f"Deleted: {path}"
    except Exception as ex:
        return False, f"[ERROR] Failed to delete {path}: {ex}"


def prompt_yes_no(question: str) -> bool:
    answer = input(f"{question} [y/N]: ").strip().lower()
    return answer in ("y", "yes")


def parse_args(argv: List[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="clean_all_slprj",
        description="Delete all 'slprj' folders in a given directory (and optionally in its subdirectories).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--dir", "-d", required=True, help="Root directory to scan.")
    p.add_argument("-r", "--recursive", action="store_true", help="Recurse into subdirectories.")
    p.add_argument("--dry-run", action="store_true", help="Show what would be deleted without deleting.")
    p.add_argument("--force", action="store_true", help="Do not prompt for confirmation.")
    p.add_argument("--verbose", action="store_true", help="Print extra details.")
    p.add_argument("--quiet", action="store_true", help="Minimal output.")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return p.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)

    root = Path(args.dir).expanduser()
    if not root.exists():
        print(f"[ERROR] Directory not found: {root}", file=sys.stderr)
        return 2
    if not root.is_dir():
        print(f"[ERROR] Not a directory: {root}", file=sys.stderr)
        return 2

    if args.verbose and not args.quiet:
        print(f"[INFO] Root: {root}")
        print(f"[INFO] Recursive: {args.recursive}")
        print(f"[INFO] Dry-run: {args.dry_run}")
        print(f"[INFO] Force: {args.force}")

    targets = find_slprj_dirs(root, recursive=args.recursive)

    if not args.quiet:
        print(f"Found {len(targets)} '{SLPRJ_NAME}' folder(s).")
        for p in targets:
            print(f" - {p}")

    if not targets:
        return 0

    if args.dry_run:
        if not args.quiet:
            print("\n[DRY-RUN] No changes made.")
        return 0

    if not args.force:
        if not prompt_yes_no(f"\nDelete {len(targets)} folder(s) named '{SLPRJ_NAME}'?"):
            print("Aborted.")
            return 0

    ok_count = 0
    fail_count = 0
    for p in targets:
        ok, msg = delete_dir(p, verbose=args.verbose and not args.quiet)
        if not args.quiet:
            print(msg)
        if ok:
            ok_count += 1
        else:
            fail_count += 1

    if not args.quiet:
        print(f"\nDone. Deleted: {ok_count}, Failed: {fail_count}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
