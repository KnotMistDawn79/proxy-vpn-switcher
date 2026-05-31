import subprocess
import platform
from typing import Optional

class ProxySwitcher:
    def __init__(self, proxy_url: str):
        self.proxy_url = proxy_url

    def enable(self) -> bool:
        try:
            if platform.system() == "Windows":
                subprocess.run(["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                               "/v", "ProxyServer", "/t", "REG_SZ", "/d", self.proxy_url, "/f"], check=True)
                subprocess.run(["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                               "/v", "ProxyEnable", "/t", "REG_DWORD", "/d", "1", "/f"], check=True)
            else:
                # Basic Linux/MacOS proxy setup (example for environment variables)
                subprocess.run(["export", f"http_proxy={self.proxy_url}"], shell=True)
                subprocess.run(["export", f"https_proxy={self.proxy_url}"], shell=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def disable(self) -> bool:
        try:
            if platform.system() == "Windows":
                subprocess.run(["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                               "/v", "ProxyEnable", "/t", "REG_DWORD", "/d", "0", "/f"], check=True)
            else:
                subprocess.run(["unset", "http_proxy"], shell=True)
                subprocess.run(["unset", "https_proxy"], shell=True)
            return True
        except subprocess.CalledProcessError:
            return False

class VPNSwitcher:
    def __init__(self, vpn_command: str):
        self.vpn_command = vpn_command

    def connect(self) -> bool:
        try:
            subprocess.run(self.vpn_command.split(), check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def disconnect(self) -> bool:
        try:
            subprocess.run(["pkill", "-f", self.vpn_command.split()[0]], check=True)
            return True
        except subprocess.CalledProcessError:
            return False