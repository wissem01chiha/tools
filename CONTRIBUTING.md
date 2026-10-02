# Contribution Guide

## Issues

## Pull Requests

### Naming Style Conventions

- Use lowercase names for scripts and folders.
- Use only hyphens (`-`) to separate words in standalone script filenames and folder names (example, `run-common-tests.sh` or `static-analysis/`). 
- Use the same descriptive basename for implementations of the same script in different shells or platforms; use the file extension to identify the implementation (for example, `run-tests.sh`, `run-tests.bat`, and `run-tests.ps1`). Add a platform qualifier only when multiple implementations use the same file extension.
- For Python files intended to be imported as modules, use Python's `snake_case` naming convention because hyphens cannot be used in import names. Standalone Python scripts follow the general hyphenated filename convention.
- Use clear action-oriented names where appropriate, such as `generate-coverage-report.sh` or `update-version.py`. Avoid vague names, unexplained abbreviations, spaces, and names like `script1` or `new-script`.
- Do not rename vendored files to match these rules; preserve upstream names and layout.

If a script has platform-specific variants or needs supporting files, keep those versions together in the folder for that task and document supported platforms, shells, prerequisites, and usage in a nearby README.

## Commit Message Style