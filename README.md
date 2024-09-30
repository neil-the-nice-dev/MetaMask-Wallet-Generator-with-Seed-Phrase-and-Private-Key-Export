# MetaMask-Wallet-Generator-with-Seed-Phrase-and-Private-Key-Export
This project is a Python-based Ethereum wallet generator compatible with MetaMask. It allows you to generate multiple wallets simultaneously. The generated wallets are automatically saved to a CSV file

# MetaMask Wallet Generator with Seed Phrase and Private Key Export

## Project Description:
This project is a Python-based Ethereum wallet generator compatible with MetaMask. It allows you to generate multiple wallets simultaneously, exporting critical information such as the public address, private key, mnemonic seed phrase, and additional details like creation date and the derivation path used.

The generated wallets are automatically saved to a CSV file, enabling you to store and reuse the information for importing wallets into MetaMask or any other Ethereum-compatible application.
#### OUT PUT CODE EXEMPLE : 

| Wallet ID | Address                                    | Private Key                                     | Mnemonic Phrase                                           | Creation Date           | Derivation Path     |
|-----------|--------------------------------------------|-------------------------------------------------|-----------------------------------------------------------|-------------------------|---------------------|
| 1         | 0xA0dFcEFABd6145194954A875f36Fa2F7F1fDE1b1 | 0x4c0883a69102937d62314444ec6602dd58b368c9cd76243b5827ed2e54cf73d2 | oblige ahead spray common wing bread below jar reason snap elbow coyote | 2024-09-30 15:27:12 | m/44'/60'/0'/0/0    |
| 2         | 0x3bE1949e7E7bB965C7b2379cE6F8b2752541fFaA | 0xe6f9f28cb10728f8dbde103ec92ba776a4d4f5f9b49b1f3f3c072a3c9d6c7494 | jelly jeans excite obscure roof shoot reward shine food used middle exile | 2024-09-30 15:27:12 | m/44'/60'/0'/0/0    |



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
