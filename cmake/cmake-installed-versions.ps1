# Copyright 2025-2026, Wissem Chiha 
# 
# Distributed under the LGPL-2.1 license 
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1

# look for all installed cmake versions in the system and
# print them in a table format
# usage: .\cmake-installed-versions.ps1

$cmakeCommands = @(Get-Command -Name cmake -All -CommandType Application 
-ErrorAction SilentlyContinue)

if ($cmakeCommands.Count -eq 0) {
    Write-Host "cmake is not installed on this system."
    exit 1
}

Write-Host "installed CMake versions:"

foreach ($cmd in $cmakeCommands) {
    $versionLine = (& $cmd.Source --version | Select-Object -First 1)
    Write-Host ("{0} : {1}" -f $versionLine, $cmd.Source)
}