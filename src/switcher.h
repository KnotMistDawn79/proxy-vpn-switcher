#ifndef SWITCHER_H
#define SWITCHER_H

#include <string>

class Switcher {
public:
    void enableProxy(const std::string& proxyUrl);
    void enableVPN(const std::string& tunDevice, const std::string& ip);
    void disableAll();
};

#endif