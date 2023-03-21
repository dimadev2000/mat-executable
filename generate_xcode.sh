#!/bin/bash
echo "Generate XCode project script"
if [ -d "build" ]; then
  echo "Build folder found. Deleting..."
  rm -rf build
  echo "Build folder deleted."
else
  echo "Build folder not found. Skipping..."
fi
mkdir build
cd build
conan profile detect
conan install ..
cmake -B . -S .. -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES="conan_provider.cmake" -DCMAKE_BUILD_TYPE=Debug -G "Xcode"