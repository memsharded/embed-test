cmake_minimum_required(VERSION 3.1)
project(embedTest CXX)

add_library(mymath STATIC mymath.cpp)
add_library(myphsx SHARED myphsx.cpp)

add_executable(myapp myapp.cpp)
target_link_libraries(myapp PRIVATE mymath myphsx)