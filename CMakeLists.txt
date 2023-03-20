cmake_minimum_required (VERSION 3.8)

project ("matexecutable")

add_subdirectory(cgcustommath)

# Add source to this project's executable.
add_executable(matexecutable "main.cpp")

target_link_libraries(matexecutable cgcustommath)

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET matexecutable PROPERTY CXX_STANDARD 20)
endif()

target_include_directories(matexecutable PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/cgcustommath)
