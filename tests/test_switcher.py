import unittest
from unittest.mock import patch
from proxy_vpn_switcher.switcher import ProxySwitcher, VPNSwitcher

class TestProxySwitcher(unittest.TestCase):
    @patch("subprocess.run")
    def test_enable_windows(self, mock_run):
        mock_run.return_value.returncode = 0
        switcher = ProxySwitcher("http://proxy.example.com:8080")
        self.assertTrue(switcher.enable())
        self.assertEqual(mock_run.call_count, 2)

    @patch("subprocess.run")
    def test_disable_windows(self, mock_run):
        mock_run.return_value.returncode = 0
        switcher = ProxySwitcher("http://proxy.example.com:8080")
        self.assertTrue(switcher.disable())
        self.assertEqual(mock_run.call_count, 1)

class TestVPNSwitcher(unittest.TestCase):
    @patch("subprocess.run")
    def test_connect(self, mock_run):
        mock_run.return_value.returncode = 0
        switcher = VPNSwitcher("openvpn --config client.ovpn")
        self.assertTrue(switcher.connect())
        mock_run.assert_called_once()

    @patch("subprocess.run")
    def test_disconnect(self, mock_run):
        mock_run.return_value.returncode = 0
        switcher = VPNSwitcher("openvpn --config client.ovpn")
        self.assertTrue(switcher.disconnect())
        mock_run.assert_called_once_with(["pkill", "-f", "openvpn"], check=True)

if __name__ == "__main__":
    unittest.main()