from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import os
import secrets

# =====================================================
# PUT YOUR REAL 64-HEX BITCOIN PRIVATE KEY HERE
# =====================================================
REAL_BTC_PRIVKEY = "PUT_YOUR_REAL_64_HEX_PRIVATE_KEY_HERE"

# Strong random-style passphrase
PASSPHRASE = (
    "exampleexampleexampleexampleexample"
)

salt = os.urandom(32)
kdf = Scrypt(
    salt=salt,
    length=32,
    n=2**18,  
    r=8,
    p=1,
)

key = kdf.derive(PASSPHRASE.encode())

# =====================================================
# AES-256-GCM (authenticated encryption)
# =====================================================
aesgcm = AESGCM(key)
nonce = os.urandom(12)

decoy = secrets.token_hex(32)

plaintext = f"""
REAL_KEY={REAL_BTC_PRIVKEY}
DECOY={decoy}
""".encode()

encrypted = aesgcm.encrypt(nonce, plaintext, None)

with open("prize.enc", "wb") as f:
    f.write(salt + nonce + encrypted)

print("✅ Secure encrypted file created: prize.enc")
print("Salt:", salt.hex())
print("Nonce:", nonce.hex())
print()
print("KEEP THIS PASSPHRASE SECRET:")
print(PASSPHRASE)
