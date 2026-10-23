# Copyright 2025-2026, Wissem Chiha 
# 
# Distributed under the LGPL-2.1 license 
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1


# ============================================================
# Shell Script for Automated Artifact Folder Tree Structure Generation
# from Activities Pre-Delivery Files
#
# 23-7-2025 : Added Zip feature and delete temp files
#
# Written by: Wissem Chiha
# Last Modified: 23-7-2025
# ============================================================

set -e  # Exit on error
shopt -s nullglob  # Avoid literal pattern if no files match

# === Define paths ===
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Creating new Artifact folder..."
read -p "Enter the model name: " MODEL_NAME

# === Define paths ===
SOURCE_DIR="$BASE_DIR/$MODEL_NAME/R2022b"
ARTIFACT_DIR="$BASE_DIR/${MODEL_NAME}_ARTIFACT"
PACKAGE_NAME="${MODEL_NAME}_SWPackage"
AUTOSAR_DIR="$SOURCE_DIR/$PACKAGE_NAME/${MODEL_NAME}_ac_autosar_rtw"
SWC_DIR="$ARTIFACT_DIR/${MODEL_NAME}_SwSrc"
REPORT_DIR="$ARTIFACT_DIR/Report"
TARGET_DIR="$ARTIFACT_DIR/$PACKAGE_NAME"
ZIP_PATH="$(command -v zip)"  # Uses zip utility

echo "The source directory is: $SOURCE_DIR"

# === Create artifact directory ===
mkdir -p "$ARTIFACT_DIR"

# === Copy model-specific package ===
cp -r "$SOURCE_DIR/$PACKAGE_NAME" "$ARTIFACT_DIR/" 2>/dev/null || true

# === Copy optional folders if they exist ===
for FOLDER in Common Production; do
    if [ -d "$SOURCE_DIR/$FOLDER" ]; then
        cp -r "$SOURCE_DIR/$FOLDER" "$ARTIFACT_DIR/"
    else
        echo "Skipping $FOLDER - not found"
    fi
done

# === Create empty folders ===
mkdir -p "$SWC_DIR"
mkdir -p "$REPORT_DIR"

# === Copy .h and .c files ===
HEADER_FILE="${MODEL_NAME}_ac.h"
SOURCE_FILE="${MODEL_NAME}_ac.c"

if [ -f "$AUTOSAR_DIR/$HEADER_FILE" ]; then
    cp "$AUTOSAR_DIR/$HEADER_FILE" "$SWC_DIR/"
else
    echo "WARNING: $HEADER_FILE not found in $AUTOSAR_DIR"
fi

if [ -f "$AUTOSAR_DIR/$SOURCE_FILE" ]; then
    cp "$AUTOSAR_DIR/$SOURCE_FILE" "$SWC_DIR/"
else
    echo "WARNING: $SOURCE_FILE not found in $AUTOSAR_DIR"
fi

# === Copy .ddf and .a2l files ===
DDF_FILE="${MODEL_NAME}.ddf"
A2L_FILE="${MODEL_NAME}_ac.a2l"

if [ -f "$SOURCE_DIR/$DDF_FILE" ]; then
    cp "$SOURCE_DIR/$DDF_FILE" "$SWC_DIR/"
else
    echo "WARNING: $DDF_FILE not found in $SOURCE_DIR"
fi

if [ -f "$SOURCE_DIR/$A2L_FILE" ]; then
    cp "$SOURCE_DIR/$A2L_FILE" "$SWC_DIR/"
else
    echo "WARNING: $A2L_FILE not found in $SOURCE_DIR"
fi

# === Move .html and Excel files to REPORT_DIR ===
echo "Moving report files to $REPORT_DIR..."

# Move only top-level .html files
for f in "$SOURCE_DIR"/*.html; do
    cp "$f" "$REPORT_DIR/" 2>/dev/null || true
done

# Move top-level Excel files
for f in "$SOURCE_DIR"/*.xls "$SOURCE_DIR"/*.xlsx; do
    cp "$f" "$REPORT_DIR/" 2>/dev/null || true
done

# === Delete .h and .slxc files in top-level of TARGET_DIR ===
find "$TARGET_DIR" -maxdepth 1 -type f \( -name "*.h" -o -name "*.slxc" \) -exec rm -f {} +

# === Check if zip is available ===
if ! command -v zip &>/dev/null; then
    echo "ERROR: zip is not installed. Please install it using your package manager."
    exit 1
fi

# === Create zip file ===
ZIP_OUTPUT="$BASE_DIR/${MODEL_NAME}.zip"
echo "Zipping artifact to: $ZIP_OUTPUT"
(cd "$ARTIFACT_DIR" && zip -r "$ZIP_OUTPUT" .) >/dev/null

echo "Artifact folder generated at: $ZIP_OUTPUT"
echo "Please move it to the appropriate directory or deliver it!"

# === Remove temporary files ===
echo "Removing temporary files..."
rm -rf "$ARTIFACT_DIR"
