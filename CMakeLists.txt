cmake_minimum_required(VERSION 3.10)
project(proxy-vpn-switcher)

set(CMAKE_CXX_STANDARD 17)

add_executable(proxy-vpn-switcher
    src/main.cpp
    src/switcher.cpp
    src/network_utils.cpp
)

target_include_directories(proxy-vpn-switcher PRIVATE src)
target_link_libraries(proxy-vpn-switcher PRIVATE pthread)