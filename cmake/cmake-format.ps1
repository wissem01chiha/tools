# Copyright 2025-2026, Wissem Chiha 
# 
# Distributed under the LGPL-2.1 license 
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1

# This is a helper script to format all cmake files using 
# cmake-format tool, given a directory name it looks 
# recursively for all cmake files and formats them in place.
# usage:
# .\cmake-format.ps1  cmake common
# this script require cmake-format tool to be installed and 
# available in the PATH environment variable.

if ($args.Count -lt 1) {
	Write-Host "cmake-format.ps1 : please provide a directory name."
	exit 1
}

$arg1 = $args[0]

# look for all CMakeLists.txt files
$cmake = Get-ChildItem -Path $arg1 -Filter CMakeLists.txt -Recurse -ErrorAction SilentlyContinue -Force
# look for all *.cmake files
$cmakeFiles = Get-ChildItem -Path $arg1 -Filter *.cmake -Recurse -ErrorAction SilentlyContinue -Force

# format all found files in place
foreach ($file in $cmake) {
	cmake-format -i $file.FullName
}
foreach ($file in $cmakeFiles) {
	cmake-format -i $file.FullName
}
