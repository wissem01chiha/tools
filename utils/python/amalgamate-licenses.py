# Copyright 2025-2026, Wissem Chiha
#
# Distributed under the LGPL-2.1 license
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1

# This script is used to generate a Licenses folder from a given
# directory containing mostly third-party software packages. It
# scans the directory recursively and copies all relevant license
# files into a mirrored directory tree under a folder called
# "Licenses".

from __future__ import annotations

import argparse
import sys
