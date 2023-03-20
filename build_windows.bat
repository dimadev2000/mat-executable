@echo off
title CMake build script
if exist build (
  echo Build folder found. Deleting...
  rmdir /s /q build
  echo Build folder deleted.
) else (
  echo Build folder not found. Skipping...
)
mkdir build
conan profile detect
conan install .
cmake -B build -S . -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES="conan_provider.cmake" -DCMAKE_BUILD_TYPE=Debug
cmake --build .\build\ --config Debug
echo Build completed!