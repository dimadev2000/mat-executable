@echo off
title Generate CMake project VS
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
cmake -B build -S . --preset x64-debug
echo Generate completed!