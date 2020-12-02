set(CMAKE_CXX_COMPILER_WORKS 1)
set(CMAKE_C_COMPILER_WORKS 1)
set(CMAKE_CXX_ABI_COMPILED 1)
set(CMAKE_C_ABI_COMPILED 1)

cmake_minimum_required(VERSION 3.1)
project(embedTest C CXX)

add_library(jmetadata OBJECT ${CMAKE_BINARY_DIR}/jmetadata.c)
add_library(mymath STATIC mymath.cpp)
add_library(myphsx SHARED myphsx.cpp)

target_link_libraries(mymath PRIVATE jmetadata)
target_link_libraries(myphsx PRIVATE jmetadata)

add_executable(myapp myapp.cpp)
target_link_libraries(myapp PRIVATE mymath myphsx jmetadata)