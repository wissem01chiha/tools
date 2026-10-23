@REM Copyright 2025-2026, Wissem Chiha
@REM
@REM Distributed under the LGPL-2.1 license
@REM (See accompanying file LICENSE or copy at
@REM https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
@REM
@REM SPDX-License-Identifier: LGPL-2.1

:: ===================================================================
:: Batch Script for Checking Cygwin Installation/Version on Win32 
:: Platform
:: ===================================================================
@echo off
setlocal enabledelayedexpansion

:: === Set Default Cygwin Installation Path === 
set CYGWIN_INSTALL_DIR=C:\cygwin64\bin
set CYGCHECK_PATH=%CYGWIN_INSTALL_DIR%\cygcheck.exe
set CYGWIN_INSTALLED=0

echo Checking for Cygwin ...
echo Using default installation directory: %CYGWIN_INSTALL_DIR%

:: Check if cygcheck.exe exists
if exist "%CYGCHECK_PATH%" (
    echo Cygwin found. Verifying installation ...

    "%CYGCHECK_PATH%" -c cygwin >nul 2>&1
    if %errorlevel%==0 (
        echo Cygwin is properly installed. Version info:
        "%CYGCHECK_PATH%" -c cygwin
        set CYGWIN_INSTALLED=1
    ) else (
        echo Cygwin check failed. Please verify the installation.
    )
) else (
    echo Cygwin not found at the default path.
    echo Please install Cygwin or check the installation directory.
)