# CMakeList.txt : CMake project for cgcustommath, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

project ("cgcustommath")

find_package(Eigen3 CONFIG REQUIRED)

# Add source to this project's executable.
add_library (cgcustommath STATIC "cgcustommath.cpp")
target_link_libraries(cgcustommath PUBLIC Eigen3::Eigen)

if(CMAKE_SYSTEM_NAME STREQUAL "Windows")
  message(STATUS "Building for Windows")
  include(${CMAKE_EIGEN3_TARGETS_PATH})
elseif(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
  message(STATUS "Building for MacOS")
  include(${CMAKE_BINARY_DIR}/conan/build/generators/Eigen3Targets.cmake)
endif()
set(EIGEN3_INCLUDE_DIR ${eigen_INCLUDE_DIRS_RELEASE})

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET cgcustommath PROPERTY CXX_STANDARD 20)
endif()

target_include_directories(cgcustommath PRIVATE ${EIGEN3_INCLUDE_DIR})
