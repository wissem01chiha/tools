# Copyright 2025-2026, Wissem Chiha 
# 
# Distributed under the LGPL-2.1 license 
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1


echo "Running pre-commit checks..."

FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.sh$')
if [ -n "$FILES" ]; then
    shellcheck $FILES || {
        echo "Shellcheck failed. Fix issues before committing."
        exit 1
    }
fi

echo "All checks passed!"
