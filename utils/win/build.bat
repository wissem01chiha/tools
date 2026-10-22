:: ===================================================================
:: Batch Script for Automated Artifact Folder Tree Structure Generation
:: from Activities Pre-Delivery Files
:: 
:: 23-7-2025 : Added Zip feature and delete temp files 
::
:: Written by: Wissem Chiha
:: Last Modified: 23-7-2025
:: ===================================================================
@echo off
setlocal enabledelayedexpansion

:: === Define paths ===
set BASE_DIR=%~dp0

echo Creating new Artifact folder...
:: === Input model name ===
set /p MODEL_NAME=Enter the model name : 

:: === Define paths ===
set SOURCE_DIR=%BASE_DIR%%MODEL_NAME%\R2022b
set ARTIFACT_DIR=%BASE_DIR%%MODEL_NAME%_ARTIFACT
set PACKAGE_NAME=%MODEL_NAME%_SWPackage
set AUTOSAR_DIR=%SOURCE_DIR%\%PACKAGE_NAME%\%MODEL_NAME%_ac_autosar_rtw
set SWC_DIR=%ARTIFACT_DIR%\%MODEL_NAME%_SwSrc
set REPORT_DIR=%ARTIFACT_DIR%\Report
set TARGET_DIR=%ARTIFACT_DIR%\%PACKAGE_NAME%
set ZIP_PATH="C:\Program Files\7-Zip\7z.exe"

echo The source directory for looking %SOURCE_DIR%
:: === Create artifact directory ===
mkdir "%ARTIFACT_DIR%"

:: === Copy model-specific package ===
xcopy /E /I /Y "%SOURCE_DIR%\%PACKAGE_NAME%" "%ARTIFACT_DIR%\%PACKAGE_NAME%" >nul 2>&1

:: === Copy optional folders if they exist ===
for %%F in (Common Production) do (
    if exist "%SOURCE_DIR%\%%F" (
        xcopy /E /I /Y "%SOURCE_DIR%\%%F" "%ARTIFACT_DIR%\%%F" >nul 2>&1
    ) else (
        echo Skipping %%F - not found
    )
)

:: === Create empty folders ===
mkdir %SWC_DIR%
mkdir %REPORT_DIR%

:: === Copy .h and .c files ===
set HEADER_FILE=%MODEL_NAME%_ac.h
set SOURCE_FILE=%MODEL_NAME%_ac.c

if exist "%AUTOSAR_DIR%\%HEADER_FILE%" (
    copy /Y "%AUTOSAR_DIR%\%HEADER_FILE%" "%SWC_DIR%" >nul 2>&1
) else (
    echo WARNING: %HEADER_FILE% not found in %AUTOSAR_DIR%
)

if exist "%AUTOSAR_DIR%\%SOURCE_FILE%" (
    copy /Y "%AUTOSAR_DIR%\%SOURCE_FILE%" "%SWC_DIR%" >nul 2>&1
) else (
    echo WARNING: %SOURCE_FILE% not found in %AUTOSAR_DIR%
)

:: === Copy .ddf and .a2l files ===
set DDF_FILE=%MODEL_NAME%.ddf
set A2L_FILE=%MODEL_NAME%_ac.a2l

if exist "%SOURCE_DIR%\%DDF_FILE%" (
    copy /Y "%SOURCE_DIR%\%DDF_FILE%" "%SWC_DIR%" >nul 2>&1
) else (
    echo WARNING: %DDF_FILE% not found in %AUTOSAR_DIR%
)

if exist "%SOURCE_DIR%\%A2L_FILE%" (
    copy /Y "%SOURCE_DIR%\%A2L_FILE%" "%SWC_DIR%" >nul 2>&1
) else (
    echo WARNING: %A2L_FILE% not found in %AUTOSAR_DIR%
)

:: === Move .html and Excel files to REPORT_DIR ===
echo Moving report files to %REPORT_DIR%...

:: Move only top-level .html files
for %%f in ("%SOURCE_DIR%\*.html") do (
   copy /Y "%%f" "%REPORT_DIR%" >nul 2>&1
)

:: Move only top-level Excel files
for %%f in ("%SOURCE_DIR%\*.xls") do (
   copy /Y "%%f" "%REPORT_DIR%" >nul 2>&1
)
for %%f in ("%SOURCE_DIR%\*.xlsx") do (
   copy /Y "%%f" "%REPORT_DIR%" >nul 2>&1
)

:: === Delete .h files in top-level only ===
for %%f in ("%TARGET_DIR%\*.h") do (
    del /F /Q "%%f" >nul 2>&1
)

:: === Delete .slxc files in top-level only ===
for %%f in ("%TARGET_DIR%\*.slxc") do (
    del /F /Q "%%f" >nul 2>&1
)

:: === Check if 7-Zip is installed ===

if not exist %ZIP_PATH% (
    echo ERROR: 7-Zip is not installed at %ZIP_PATH%
    echo Please install 7-Zip or update the script with the correct path.
    pause
    exit /b
)

%ZIP_PATH% a -tzip "%BASE_DIR%%MODEL_NAME%.zip" "%ARTIFACT_DIR%\*" >nul 2>&1

echo Artifact folder Generated at: %BASE_DIR%%MODEL_NAME%.zip
echo Please move it to the appropriate directory or deliver it !

echo Removing temporary files...
rmdir /S /Q "%ARTIFACT_DIR%" >nul 2>&1

pause
