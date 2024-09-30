# MetaMask-Wallet-Generator-with-Seed-Phrase-and-Private-Key-Export
This project is a Python-based Ethereum wallet generator compatible with MetaMask. It allows you to generate multiple wallets simultaneously. The generated wallets are automatically saved to a CSV file

# MetaMask Wallet Generator with Seed Phrase and Private Key Export

## Project Description:
This project is a Python-based Ethereum wallet generator compatible with MetaMask. It allows you to generate multiple wallets simultaneously, exporting critical information such as the public address, private key, mnemonic seed phrase, and additional details like creation date and the derivation path used.

The generated wallets are automatically saved to a CSV file, enabling you to store and reuse the information for importing wallets into MetaMask or any other Ethereum-compatible application.

## Features:
- Generate multiple Ethereum wallets compatible with MetaMask.
- Export wallet details to a CSV file, including:
  - Unique Wallet ID for each generated wallet.
  - Public Ethereum address.
  - Private key (in hexadecimal format).
  - Mnemonic seed phrase (BIP-39) to restore the wallet.
  - Creation date and time of each wallet.
  - BIP-44 derivation path used for generating addresses.
- Easily export and manage multiple wallets.

## How to Use:

### 1. Install the required dependencies:
```bash
pip install bip-utils pandas
