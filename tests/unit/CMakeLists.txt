cmake_minimum_required(VERSION 3.12)

include(Variables)

set(PROJECT_NAME ${PROJECT_NAME}_unittest)

project(${PROJECT_NAME} CXX)

file(GLOB_RECURSE SOURCES src/*.cpp)

# Unit Tests
add_executable(${PROJECT_NAME} ${SOURCES})

target_link_libraries(${PROJECT_NAME} PRIVATE ${PROJECT_NAME_AS_LIBRARY} userver-utest)
add_google_tests(${PROJECT_NAME})
