:: ===================================================================
:: Batch Script for Checking Cygwin Instllation/Version on Win32 
:: Platform
::
:: Written by: Wissem Chiha
:: Last Modified: 23-7-2025
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