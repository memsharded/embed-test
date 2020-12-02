cmake_minimum_required(VERSION 3.1)
project(embedTest C CXX)

add_library(metadata OBJECT data.c)
add_library(mymath STATIC mymath.cpp)
add_library(myphsx SHARED myphsx.cpp)

target_link_libraries(mymath PRIVATE metadata)
target_link_libraries(myphsx PRIVATE metadata)

add_executable(myapp myapp.cpp)
target_link_libraries(myapp PRIVATE mymath myphsx metadata)