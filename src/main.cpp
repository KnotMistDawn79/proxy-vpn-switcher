#include <iostream>
#include "switcher.h"

int main() {
    std::cout << "Proxy/VPN Switcher\n";
    std::cout << "1. Enable Proxy\n";
    std::cout << "2. Enable VPN\n";
    std::cout << "3. Disable All\n";
    std::cout << "Choose option: ";

    int choice;
    std::cin >> choice;

    Switcher switcher;
    switch (choice) {
        case 1:
            switcher.enableProxy("http://proxy.example.com:8080");
            break;
        case 2:
            switcher.enableVPN("/dev/net/tun", "10.8.0.1");
            break;
        case 3:
            switcher.disableAll();
            break;
        default:
            std::cout << "Invalid choice\n";
    }

    return 0;
}