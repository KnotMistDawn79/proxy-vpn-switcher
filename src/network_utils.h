#ifndef NETWORK_UTILS_H
#define NETWORK_UTILS_H

#include <string>

namespace NetworkUtils {
    bool setProxy(const std::string& proxyUrl);
    bool setupTunDevice(const std::string& tunDevice, const std::string& ip);
    bool disableNetworkSettings();
}

#endif