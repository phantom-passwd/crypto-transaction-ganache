# Ganache Crypto Transaction 🚀

A Python module for managing and sending cryptocurrency transactions using Web3.py for testnet crypto. This module supports Ethereum transactions (Ganache ).

## Features ✨
- Check account balance
- Send Ethereum transactions
- Easily configurable via JSON file

## Installation 📦

1. Clone the repository:
    ```bash
    git clone https://github.com/phantom-passwd/crypto-transaction.git
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

Create a `conf.json` file in the root directory with the following content (or just modify the one in the repo):
```json
{
    "crypto": "eth",
    //wallet That receive the funds
    "adress": "0xE92B321D521Cf952DEf6F8AAE73A5E59896E4Fe4"
}
```

## Usage 🛠️

1. Import the `CryptoTransaction` class and create an instance:
    ```python
    from crypto import CryptoTransaction

    # Initialize with configuration file
    crypto_tx = CryptoTransaction('conf.json')

    # Set account and private key
    crypto_tx.set_account("0x6c6FF6805198918981UYdz6516b7465c94264", "0x41e2a9fa6aea354f303ce87ef1ezf181FEZFZF818866c4c9f82938e686809")

    # Send transaction !!!
    crypto_tx.send_transaction()
    ```

2. Run the script:
    ```bash
    python crypto.py
    ```

## License 📄

This project is licensed under License - see the LICENSE file for details.

## Contributing 🤝

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact 📧

DM >> phantoms_._   on discord

---
😄
