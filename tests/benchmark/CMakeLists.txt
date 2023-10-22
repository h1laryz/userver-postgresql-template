cmake_minimum_required(VERSION 3.12)
include(Variables)

set(PROJECT_NAME ${PROJECT_NAME}_benchmark)

project(${PROJECT_NAME} CXX)

file(GLOB_RECURSE SOURCES src/*.cpp)

# Benchmarks
add_executable(${PROJECT_NAME} ${SOURCES})

target_link_libraries(${PROJECT_NAME} PRIVATE ${PROJECT_NAME_AS_LIBRARY} userver-ubench)
target_include_directories(${PROJECT_NAME} PRIVATE include)
add_google_benchmark_tests(${PROJECT_NAME})
