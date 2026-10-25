# Copyright 2025-2026, Wissem Chiha 
# 
# Distributed under the LGPL-2.1 license 
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1

set -e

########################################################################
# Script for running all modules tests and collecting coverage.
########################################################################

COLOR_OFF="\033[0m"
RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"

fatal() {
    echo -e >&2 "${RED}[FATAL] : $*${COLOR_OFF}"
    exit 1
}

info() {
    echo -e "[INFO] : $*"
}

success() {
    echo -e "[INFO] : $* ${GREEN}OK${COLOR_OFF}"
}

# Check CTest
CTEST=$(command -v ctest || true)
if [ -z "$CTEST" ]; then
    fatal "ctest not found in path, install CMake/CTest."
fi

# Default build directory
BUILDDIR="${1:-build}"

if [ ! -d "$BUILDDIR" ]; then
    fatal "Build directory not found: $BUILDDIR"
fi

info "Running tests in build directory: $BUILDDIR"

(cd "$BUILDDIR" && $CTEST --output-on-failure)

success "tests executed."

info "Collecting coverage..."
(cd "$BUILDDIR" && $CTEST -T coverage)

success "Coverage report generated in: $BUILDDIR/Testing/Temporary"
