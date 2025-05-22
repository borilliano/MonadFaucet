
# MonadFaucet

**Auto Faucet Request for Monad Testnet**

## Overview

**MonadFaucet** is a Python automation script that helps developers and testers automatically request Monad testnet tokens from the [Monad Faucet](https://faucet.monad.xyz/). This tool streamlines the process of acquiring testnet tokens for smart contract development and testing on the Monad network.

## Features

- Automates navigation to the Monad Faucet and initiates the wallet connection process
- Uses browser automation for a simple, user-friendly experience
- Saves time for developers and testers

## Prerequisites

- Python 3.7 or higher
- [pip](https://pip.pypa.io/en/stable/)
- [pyppeteer](https://github.com/pyppeteer/pyppeteer) Python package

## Installation

Clone this repository:

```bash
git clone https://github.com/borilliano/MonadFaucet.git
cd MonadFaucet
```

Install dependencies:

```bash
pip install pyppeteer
```

## Usage

1. Open `mon.py` and review the script.
2. Run the script:

```bash
python mon.py
```

The script will launch a browser, navigate to the Monad Faucet, and click the "Connect Wallet" button.  
**Note:** You will need to complete the wallet connection and token request manually in the browser window.

## Notes

- **Wallet Connection:** This script does **not** automate wallet extension interactions (like MetaMask). For full automation, consider Node.js with Puppeteer and dappeteer.
- **Selectors:** If the faucet website changes, you may need to update the selectors in `mon.py`.
- **Responsible Use:** Please use this tool responsibly and do not abuse public testnet faucets.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
