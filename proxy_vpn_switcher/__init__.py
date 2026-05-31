from .switcher import ProxySwitcher, VPNSwitcher
from .config import load_config, save_config

__all__ = ["ProxySwitcher", "VPNSwitcher", "load_config", "save_config"]
__version__ = "0.1.0"