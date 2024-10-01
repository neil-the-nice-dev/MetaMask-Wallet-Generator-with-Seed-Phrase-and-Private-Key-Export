# MetaMask Wallet Generator with Complex Password and Private Key Export

## Description:
This project is a Python-based Ethereum wallet generator compatible with MetaMask. It allows you to generate multiple wallets at once, exporting essential information such as the public address, private key, mnemonic seed phrase, and additional details like a highly complex password, creation date, and the derivation path used.

The generated wallets are automatically saved to a CSV file, making it easy to store and reuse the information for importing wallets into MetaMask or any other Ethereum-compatible application.

## Features:
- Generate multiple Ethereum wallets compatible with MetaMask.
- Export wallet details to a CSV file, including:
  - Unique Wallet ID for each generated wallet.
  - Public Ethereum address.
  - Private key (in hexadecimal format).
  - Mnemonic seed phrase (BIP-39) to restore the wallet.
  - Highly complex random password (32 characters).
  - Creation date and time of each wallet.
  - BIP-44 derivation path used for generating addresses.
- Easily export and manage multiple wallets.

## How to Use:

1. **Install the required dependencies:**

   ```bash
   pip install bip-utils pandas

#### OUT PUT CODE EXEMPLE : 

| Wallet ID | Address                                    | Private Key                                     | Mnemonic Phrase                                           | Creation Date           | Derivation Path     | Password                          |
|-----------|--------------------------------------------|-------------------------------------------------|-----------------------------------------------------------|-------------------------|---------------------|------------------------------------|
| 1         | 0xA0dFcEFABd6145194954A875f36Fa2F7F1fDE1b1 | 0x4c0883a69102937d62314444ec6602dd58b368c9cd76243b5827ed2e54cf73d2 | oblige ahead spray common wing bread below jar reason snap elbow coyote | 2024-09-30 15:27:12      | m/44'/60'/0'/0/0    | &5tL%8xW7Yv*G4kJZ^3p!2aT9r@hVbF    |
| 2         | 0x3bE1949e7E7bB965C7b2379cE6F8b2752541fFaA | 0xe6f9f28cb10728f8dbde103ec92ba776a4d4f5f9b49b1f3f3c072a3c9d6c7494 | jelly jeans excite obscure roof shoot reward shine food used middle exile | 2024-09-30 15:27:12      | m/44'/60'/0'/0/0    | *xR@4vZ8yP!Xc5JdQ#3fN6bT$L7kG1aM    |

