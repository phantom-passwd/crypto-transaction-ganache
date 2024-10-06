import json
from web3 import Web3

class CryptoTransaction:
    def __init__(self, conf_file):
        with open(conf_file) as f:
            conf = json.load(f)
            self.crypto = conf['crypto']
            self.address = conf['adress']
        self.web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
        self.acc1 = None
        self.acc1_pk = None

    def set_account(self, acc1, acc1_pk):
        self.acc1 = acc1
        self.acc1_pk = acc1_pk

    def balance(self, address):
        balance = self.web3.eth.get_balance(address)
        balance_eth = self.web3.from_wei(balance, "ether")
        print(f"balance of {address} >> {balance_eth}")

    def send_transaction(self):
        if not self.acc1 or not self.acc1_pk:
            raise ValueError("Account and private key must be set before sending a transaction.")
        
        self.balance(self.acc1)
        self.balance(self.address)

        nonce = self.web3.eth.get_transaction_count(self.acc1)
        tx = {
            'nonce': nonce,
            'to': self.address,
            'gas': 200000,
            'gasPrice': self.web3.to_wei(50, "gwei")
        }

        if self.crypto == "eth":
            tx['value'] = self.web3.to_wei(10, "ether")
            print(tx)

            signed_tx = self.web3.eth.account.sign_transaction(tx, self.acc1_pk)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.raw_transaction)
            print(self.web3.to_hex(tx_hash))

        elif self.crypto == "btc":
            pass

        self.balance(self.acc1)
        self.balance(self.address)


crypto_tx = CryptoTransaction('conf.json')
crypto_tx.set_account("0x6c6FF684Ab6D60075B8b08A13D9c0b7465c94264", "0x41e2a9fa6aea354f303cefff20fac1b576dc10cead28766c4c9f82938e7a0609")
crypto_tx.send_transaction()


