cmake_minimum_required(VERSION 2.8.9)
project (hello)

SET(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -std=c++11")

add_executable(hello main.cpp)
