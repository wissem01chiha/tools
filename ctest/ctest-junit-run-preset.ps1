# Copyright 2025-2026, Wissem Chiha 
# 
# Distributed under the LGPL-2.1 license 
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1

# this script runs ctest with a given preset name
# and outputs the results in junit format to results.xml
# Usage: .\ctest-run-preset.ps1 <preset_name>

param (
    [string]$presetName = "default"
)

ctest --preset $presetName --output-junit results.xml