#include "network_utils.h"
#include <cstdlib>
#include <iostream>

namespace NetworkUtils {
    bool setProxy(const std::string& proxyUrl) {
        std::string cmd = "gsettings set org.gnome.system.proxy.http host '" + proxyUrl + "'";
        return system(cmd.c_str()) == 0;
    }

    bool setupTunDevice(const std::string& tunDevice, const std::string& ip) {
        std::string cmd = "sudo ip tuntap add dev " + tunDevice + " mode tun && "
                         "sudo ip addr add " + ip + " dev " + tunDevice + " && "
                         "sudo ip link set " + tunDevice + " up";
        return system(cmd.c_str()) == 0;
    }

    bool disableNetworkSettings() {
        return system("gsettings set org.gnome.system.proxy mode 'none'") == 0;
    }
}