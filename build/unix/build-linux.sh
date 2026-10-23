# Copyright 2025-2026, Wissem Chiha 
# 
# Distributed under the LGPL-2.1 license 
# (See accompanying file LICENSE or copy at
# https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
#
# SPDX-License-Identifier: LGPL-2.1

set -e  
BUILD_DIR="build"
CORES=$(nproc)  
mkdir -p $BUILD_DIR
cd $BUILD_DIR
cmake -G Ninja ..
ninja -j$CORES
