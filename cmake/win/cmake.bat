@REM Copyright 2025-2026, Wissem Chiha
@REM
@REM Distributed under the LGPL-2.1 license
@REM (See accompanying file LICENSE or copy at
@REM https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
@REM
@REM SPDX-License-Identifier: LGPL-2.1

@REM this is an alias for cmake.exe, 
@REM used for non-admin installations of CMake on Windows, 
@REM where the CMake bin directory is not in the PATH.
@REM update the path below to point to your CMake installation if necessary.

@echo off
"C:\Program Files\CMake\bin\cmake.exe" %*
