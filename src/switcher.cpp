#include "switcher.h"
#include "network_utils.h"
#include <iostream>

void Switcher::enableProxy(const std::string& proxyUrl) {
    if (NetworkUtils::setProxy(proxyUrl)) {
        std::cout << "Proxy enabled: " << proxyUrl << "\n";
    } else {
        std::cerr << "Failed to enable proxy\n";
    }
}

void Switcher::enableVPN(const std::string& tunDevice, const std::string& ip) {
    if (NetworkUtils::setupTunDevice(tunDevice, ip)) {
        std::cout << "VPN enabled on " << tunDevice << " with IP " << ip << "\n";
    } else {
        std::cerr << "Failed to enable VPN\n";
    }
}

void Switcher::disableAll() {
    if (NetworkUtils::disableNetworkSettings()) {
        std::cout << "All network settings disabled\n";
    } else {
        std::cerr << "Failed to disable network settings\n";
    }
}