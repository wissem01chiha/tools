# Contribution Guide

## Issues

Before opening an issue:

- Check whether the issue has already been reported.
- Verify that the problem still exists on the latest version of the repository.
- Include enough information to reproduce the problem.
- Provide the operating system, shell, tool version, and any relevant environment details.
- Include logs, error messages, screenshots, or terminal output when applicable.

When reporting a bug, please include:

- A clear and descriptive title.
- Steps to reproduce the issue.
- Expected behavior.
- Actual behavior.
- Relevant logs or error messages.

Feature requests are welcome. Please describe:

- The problem you are trying to solve.
- The proposed solution.
- Any alternative solutions you have considered.
- Example use cases.

## Pull Requests

Before submitting a pull request:

- Open an issue first for large changes or new features.
- Ensure your changes are focused and address a single topic.
- Update documentation when necessary.
- Test your changes on supported platforms whenever possible.
- Follow the repository naming conventions.
- Follow the commit message conventions described below.

Pull request descriptions should include:

- A summary of the changes.
- The motivation behind the changes.
- References to related issues.
- Relevant screenshots, logs, or examples if applicable.

Pull requests may be rejected if they:

- Introduce unnecessary complexity.
- Duplicate existing functionality.
- Lack documentation for user-facing changes.

## Naming Style Conventions

- Use lowercase names for scripts and folders.
- Use only hyphens (`-`) to separate words in standalone script filenames and folder names (for example, `run-common-tests.sh` or `static-analysis/`).
- Use the same descriptive basename for implementations of the same script in different shells or platforms; use the file extension to identify the implementation (for example, `run-tests.sh`, `run-tests.bat`, and `run-tests.ps1`). Add a platform qualifier only when multiple implementations use the same file extension.
- For Python files intended to be imported as modules, use Python's `snake_case` naming convention because hyphens cannot be used in import names. Standalone Python scripts follow the general hyphenated filename convention.
- Use clear action-oriented names where appropriate, such as `generate-coverage-report.sh` or `update-version.py`.
- Avoid vague names, unexplained abbreviations, spaces, and names such as `script1` or `new-script`.
- Do not rename vendored files to match these rules; preserve upstream names and layout.

If a script has platform-specific variants or requires supporting files, keep those versions together in the folder for that task and document supported platforms, shells, prerequisites, and usage in a nearby README.

## Commit Message Style

Although not enforced, the repository encourages the use of the Conventional Commits specification. It helps maintain a clean project history and simplifies changelog generation during releases.

Supported commit types include:

- `build`: changes to the build system or dependencies
- `chore`: routine tasks with no production code changes
- `ci`: changes to CI configuration or scripts
- `docs`: documentation-only changes
- `feat`: new feature
- `fix`: bug fix
- `perf`: performance improvements
- `refactor`: code changes that neither fix a bug nor add a feature
- `revert`: revert a previous commit
- `style`: formatting, whitespace, naming, or other non-functional changes
- `test`: adding or correcting tests