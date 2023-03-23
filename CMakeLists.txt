cmake_minimum_required (VERSION 3.8)

project ("matexecutable")

add_subdirectory(cgcustommath)
if(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
  message(STATUS "Building for MacOS")
  set(CMAKE_OSX_ARCHITECTURES "arm64;x86_64")
endif()
# Add source to this project's executable.
add_executable(matexecutable "main.cpp")
target_link_libraries(matexecutable cgcustommath)

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET matexecutable PROPERTY CXX_STANDARD 20)
endif()

target_include_directories(matexecutable PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/cgcustommath)



install(TARGETS matexecutable DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/build/bin)

