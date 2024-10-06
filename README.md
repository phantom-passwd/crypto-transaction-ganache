# Crypto Transaction 🚀

A Python module for managing and sending cryptocurrency transactions using Web3.py. This module supports Ethereum transactions and can be extended to support other cryptocurrencies.

## Features ✨
- Check account balance
- Send Ethereum transactions
- Easily configurable via JSON file

## Installation 📦

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/crypto-transaction.git
    cd crypto-transaction
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration ⚙️

Create a `conf.json` file in the root directory with the following content:
```json
{
    "crypto": "eth",
    "adress": "0xE92B321D521Cf952DEf6F8AAE73A5E59896E4Fe4"
}
