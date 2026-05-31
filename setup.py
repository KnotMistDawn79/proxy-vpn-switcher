from setuptools import setup, find_packages

setup(
    name="proxy-vpn-switcher",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "proxy-vpn-switcher=proxy_vpn_switcher.cli:main",
        ],
    },
    python_requires=">=3.6",
)