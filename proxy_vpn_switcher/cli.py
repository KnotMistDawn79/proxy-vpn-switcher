import argparse
from .switcher import ProxySwitcher, VPNSwitcher
from .config import load_config

def main():
    parser = argparse.ArgumentParser(description="Proxy/VPN Switcher")
    subparsers = parser.add_subparsers(dest="command")

    # Proxy commands
    proxy_parser = subparsers.add_parser("proxy", help="Manage proxies")
    proxy_parser.add_argument("action", choices=["enable", "disable"], help="Enable or disable proxy")
    proxy_parser.add_argument("--url", help="Proxy URL (e.g., http://proxy.example.com:8080)")

    # VPN commands
    vpn_parser = subparsers.add_parser("vpn", help="Manage VPN")
    vpn_parser.add_argument("action", choices=["connect", "disconnect"], help="Connect or disconnect VPN")
    vpn_parser.add_argument("--command", help="VPN command to execute")

    args = parser.parse_args()
    config = load_config()

    if args.command == "proxy":
        switcher = ProxySwitcher(args.url or config["proxies"][0] if config["proxies"] else None)
        if args.action == "enable":
            print("Enabling proxy..." if switcher.enable() else "Failed to enable proxy")
        else:
            print("Disabling proxy..." if switcher.disable() else "Failed to disable proxy")

    elif args.command == "vpn":
        switcher = VPNSwitcher(args.command or config["vpn_commands"][0] if config["vpn_commands"] else None)
        if args.action == "connect":
            print("Connecting VPN..." if switcher.connect() else "Failed to connect VPN")
        else:
            print("Disconnecting VPN..." if switcher.disconnect() else "Failed to disconnect VPN")

if __name__ == "__main__":
    main()