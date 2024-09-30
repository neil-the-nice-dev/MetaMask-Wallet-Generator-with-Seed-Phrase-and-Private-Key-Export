# MetaMask-Wallet-Generator-with-Seed-Phrase-and-Private-Key-Export
This project is a Python-based Ethereum wallet generator compatible with MetaMask. It allows you to generate multiple wallets simultaneously. The generated wallets are automatically saved to a CSV file

#Features:
Generate multiple Ethereum wallets compatible with MetaMask.
Export wallet details to a CSV file, including:
Unique Wallet ID for each generated wallet.
Public Ethereum address.
Private key (in hexadecimal format).
Mnemonic seed phrase (BIP-39) to restore the wallet.
Creation date and time of each wallet.
BIP-44 derivation path used for generating addresses.
Easily export and manage multiple wallets.
How to Use:
Install the required dependencies:
bash
Copy code
pip install bip-utils pandas
Run the script to generate a specified number of wallets (default is 5):
python
Copy code
python generate_wallets.py
The generated wallet details will be displayed in the terminal and saved in a CSV file named metamask_wallets_with_info.csv.
Example Use Case:
You can import the mnemonic seed phrase or the private key directly into MetaMask to restore wallets on another device.
