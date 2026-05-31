#include "../src/switcher.h"
#include "../src/network_utils.h"
#include <cassert>

void testEnableProxy() {
    Switcher switcher;
    switcher.enableProxy("http://test.proxy:8080");
    // In a real test, we'd mock NetworkUtils
}

void testEnableVPN() {
    Switcher switcher;
    switcher.enableVPN("/dev/net/tun0", "10.0.0.1");
}

void testDisableAll() {
    Switcher switcher;
    switcher.disableAll();
}

int main() {
    testEnableProxy();
    testEnableVPN();
    testDisableAll();
    return 0;
}