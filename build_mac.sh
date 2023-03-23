#!/bin/bash
echo "CMake build script"
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
conan install ../
cd ../
cmake -B build -S . -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES="conan_provider.cmake" -DCMAKE_BUILD_TYPE=Debug -G "Xcode"
cmake --build build --config Debug
cmake --install build --config Debug
echo "Build completed!"