# Functional Tests
include(UserverTestsuite)
include(Variables)

userver_testsuite_add_simple(
        SERVICE_TARGET "${PROJECT_NAME}"
        REQUIREMENTS "${CMAKE_CURRENT_SOURCE_DIR}/requirements.txt"
        CONFIG_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../../configs/static_config.yaml"
        DYNAMIC_CONFIG_FALLBACK_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../../configs/dynamic_config_fallback.json"
)
