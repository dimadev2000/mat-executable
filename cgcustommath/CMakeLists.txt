# CMakeList.txt : CMake project for cgcustommath, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

project ("cgcustommath")

find_package(Eigen3 CONFIG REQUIRED)

# Add source to this project's executable.
add_library (cgcustommath STATIC "cgcustommath.cpp")
target_link_libraries(cgcustommath PUBLIC Eigen3::Eigen)
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  message("Debug build.")
  if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    message(STATUS "Building for Linux, unsupported yet!")
  elseif(CMAKE_SYSTEM_NAME STREQUAL "Windows")
    message(STATUS "Building for Windows")
    include(${CMAKE_BINARY_DIR}/conan/build/generators/Eigen3Targets.cmake)
  elseif(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
    message(STATUS "Building for MacOS")
    include(${CMAKE_BINARY_DIR}/conan/build/Debug/generators/Eigen3Targets.cmake)
  else()
    message(STATUS "Unknown OS: ${CMAKE_SYSTEM_NAME}")
  endif()
  set(EIGEN3_INCLUDE_DIR ${eigen_INCLUDE_DIRS_DEBUG})
elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
  message("Release build.")
  if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    message(STATUS "Building for Linux, unsupported yet!")
  elseif(CMAKE_SYSTEM_NAME STREQUAL "Windows")
    message(STATUS "Building for Windows")
    include(${CMAKE_BINARY_DIR}/conan/build/generators/Eigen3Targets.cmake)
  elseif(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
    message(STATUS "Building for MacOS")
    include(${CMAKE_BINARY_DIR}/conan/build/Release/generators/Eigen3Targets.cmake)
  else()
    message(STATUS "Unknown OS: ${CMAKE_SYSTEM_NAME}")
  endif()
  set(EIGEN3_INCLUDE_DIR ${eigen_INCLUDE_DIRS_RELEASE})
else()
  message("Some other build type.")
endif()

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET cgcustommath PROPERTY CXX_STANDARD 20)
endif()

target_include_directories(cgcustommath PRIVATE ${EIGEN3_INCLUDE_DIR})

install(FILES "cgcustommath.h" DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/../build/cgcustommath/include)
install(TARGETS cgcustommath EXPORT cgcustommathConfig DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/../build/cgcustommath/lib) 
install(EXPORT cgcustommathConfig DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/../build/cgcustommath/lib/cmake) 
