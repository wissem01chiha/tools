# Copyright 2025-2026, Wissem Chiha 
# 
# Distributed under the LGPL-2.1 license 
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1

# remove-file-with-extension <extension>
# remove all file extension given the extension provided
# Usage: remove-file-extension.sh .txt
find . -name "*$1" -type f -delete