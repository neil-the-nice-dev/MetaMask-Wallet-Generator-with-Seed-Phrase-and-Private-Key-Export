import pandas as pd
from datetime import datetime
import random
import string
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

#NB Wallets
#----------------------------------------------------------------

number_of_wallets = 5 

#----------------------------------------------------------------


def generate_password(length=32):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def create_metamask_wallet(wallet_number):


    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(12)


    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()


    bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    bip44_acc = bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)


    address = bip44_acc.PublicKey().ToAddress()
    private_key = bip44_acc.PrivateKey().Raw().ToHex()


    password = generate_password()


    return {
        'Wallet ID': wallet_number,
        'Address': address,
        'Private Key': private_key,
        'Mnemonic Phrase': mnemonic,
        'Creation Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Derivation Path': "m/44'/60'/0'/0/0",
        'Password': password
    }


def generate_wallet_dataframe(number_of_wallets=2):
    wallet_list = []
    for wallet_number in range(1, number_of_wallets + 1):
        wallet_info = create_metamask_wallet(wallet_number)
        wallet_list.append(wallet_info)
    df = pd.DataFrame(wallet_list)
    return df

wallet_df = generate_wallet_dataframe(number_of_wallets)
print(wallet_df)
wallet_df.to_csv('metamask_wallets_with_info.csv', index=False)


