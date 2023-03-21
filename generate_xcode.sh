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
cmake -G "Xcode" ..