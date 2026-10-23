@REM Copyright 2025-2026, Wissem Chiha
@REM
@REM Distributed under the LGPL-2.1 license
@REM (See accompanying file LICENSE or copy at
@REM https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
@REM
@REM SPDX-License-Identifier: LGPL-2.1

@echo off
setlocal enabledelayedexpansion

set BUILD_DIR=build

if exist %BUILD_DIR% (
    rmdir /s /q %BUILD_DIR%
)
if not exist %BUILD_DIR% mkdir %BUILD_DIR%

cd %BUILD_DIR%

cmake -G Ninja -DCMAKE_BUILD_TYPE=Release ..

ninja -j4
