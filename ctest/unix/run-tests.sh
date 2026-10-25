# Copyright 2025-2026, Wissem Chiha 
# 
# Distributed under the LGPL-2.1 license 
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1

if ! command -v ctest >/dev/null 2>&1; then
  echo "ctest not found."
  exit 1
fi

cd build 

ctest -C Debug --output-on-failure
