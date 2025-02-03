import pandas as pd
from datetime import datetime
import random
import string
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
import psycopg2
from psycopg2 import sql


DB_NAME = 'wallet'
DB_USER = 'postgres'
DB_PASSWORD = 'Mafate10'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Nombre de wallets à générer

########################################################################
number_of_wallets = 5
########################################################################


def generate_password(length=32):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def create_metamask_wallet(wallet_number):
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(12)
    seed = Bip39SeedGenerator(mnemonic).Generate()
    
    bip_obj = Bip44.FromSeed(seed, Bip44Coins.ETHEREUM).DeriveDefaultPath()
    
    return {
        'Wallet ID': wallet_number,
        'Address': bip_obj.PublicKey().ToAddress(),
        'Private Key': bip_obj.PrivateKey().Raw().ToHex(),
        'Mnemonic Phrase': mnemonic,
        'Creation Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Derivation Path': "m/44'/60'/0'/0/0",
        'Password': generate_password()
    }

def generate_wallets(number):
    return pd.DataFrame([create_metamask_wallet(i+1) for i in range(number)])

try:

    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metamask_wallets (
            wallet_id INT PRIMARY KEY,
            address TEXT NOT NULL,
            private_key TEXT NOT NULL,
            mnemonic_phrase TEXT NOT NULL,
            creation_date TIMESTAMP NOT NULL,
            derivation_path TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    wallets_df = generate_wallets(number_of_wallets)
    
    for _, row in wallets_df.iterrows():
        cursor.execute("""
            INSERT INTO metamask_wallets 
            (wallet_id, address, private_key, mnemonic_phrase, creation_date, derivation_path, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Wallet ID'],
            row['Address'],
            row['Private Key'],
            row['Mnemonic Phrase'],
            row['Creation Date'],
            row['Derivation Path'],
            row['Password']
        ))
    
    conn.commit()
    print(f"{number_of_wallets} wallets sauvegardés avec succès dans PostgreSQL !")

except Exception as e:
    print(f"Erreur : {e}")
    conn.rollback()

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()