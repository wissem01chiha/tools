:: ===================================================================
:: Batch Script for Automated Update Local files from GitHub Repository
:: Written by: Wissem Chiha
:: Last Modified: 9 September 2025
:: ===================================================================

@echo off
setlocal enabledelayedexpansion

:: Global Settings 
set "BASE_BRANCH=00AF_2508A0"


git --version

cd "%~dp0ePT_HCP_AutosarMigration"

echo Fetching latest changes from remote...
git fetch --depth 1 origin

echo Resetting to latest commit on branch %BASE_BRANCH% ...
git reset --hard origin/%BASE_BRANCH%

cd "%~dp0"

echo Last update: %DATE% %TIME% > Last_Update.txt

echo Update complete.
pause
