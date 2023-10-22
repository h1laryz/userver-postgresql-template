cmake_minimum_required(VERSION 3.12)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)
include(Variables)

project(${PROJECT_NAME} CXX)

include(third_party/userver/cmake/SetupEnvironment.cmake)
include(GNUInstallDirs)

# Service as library
file(GLOB_RECURSE LIBRARY_SOURCES src/server/*.cpp)

add_library(${PROJECT_NAME_AS_LIBRARY} OBJECT ${LIBRARY_SOURCES})
target_include_directories(${PROJECT_NAME_AS_LIBRARY} PUBLIC include)
target_link_libraries(${PROJECT_NAME_AS_LIBRARY} PUBLIC userver-postgresql)

# The Service
add_executable(${PROJECT_NAME} src/main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE ${PROJECT_NAME_AS_LIBRARY})

# Userver submodule
add_subdirectory(third_party/userver)

# Install
if(DEFINED ENV{PREFIX})
  message(STATUS "Set install prefix: $ENV{PREFIX}")
  file(TO_CMAKE_PATH "$ENV{PREFIX}" PREFIX_PATH)
  set(CMAKE_INSTALL_PREFIX ${PREFIX_PATH})
endif()

set(CONFIG_FALLBACK_PATH
    "${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_SYSCONFDIR}/${PROJECT_NAME}/dynamic_config_fallback.json")

configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/configs/config_vars.template.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/configs/config_vars.yaml"
)
configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/configs/config_vars.docker.template.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/configs/config_vars.docker.yaml"
)

file(GLOB CONFIGS_FILES ${CMAKE_CURRENT_SOURCE_DIR}/configs/*.yaml ${CMAKE_CURRENT_SOURCE_DIR}/configs/*.json)

install(TARGETS ${PROJECT_NAME} DESTINATION ${CMAKE_INSTALL_BINDIR} COMPONENT ${PROJECT_NAME})
install(FILES ${CONFIGS_FILES} DESTINATION ${CMAKE_INSTALL_SYSCONFDIR}/${PROJECT_NAME} COMPONENT ${PROJECT_NAME})

# Other projects
add_subdirectory(tests/functional)
add_subdirectory(tests/unit)
add_subdirectory(tests/benchmark)
