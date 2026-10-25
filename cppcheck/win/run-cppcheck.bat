@REM Copyright 2025-2026, Wissem Chiha
@REM
@REM Distributed under the LGPL-2.1 license
@REM (See accompanying file LICENSE or copy at
@REM https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
@REM
@REM SPDX-License-Identifier: LGPL-2.1

@echo off
SETLOCAL enableDelayedExpansion

WHERE cppcheck.exe > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 (
  ECHO cppcheck.exe not found.
  EXIT /B 1
)

cppcheck ^
    --enable=all ^
    --inconclusive ^
    --std=c++11 ^
    --suppress=missingIncludeSystem ^
    --suppress=missingInclude ^
    --enable=style ^
    --enable=performance ^
    --suppress=missingSystemInclude ^
    --suppress=unmatchedSuppression ^
    --error-exitcode=1 ^
    --inline-suppr ^
    ./include/** ^
    ./example/*.cpp
