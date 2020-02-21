import os

import tinyaes
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

BLOCK_SIZE = 16


def encrypt_pycryptodomex(data, key):
    length = len(key)
    if length > BLOCK_SIZE:
        key = key[: -(length - BLOCK_SIZE)]
    if length not in (16, 24, 32):
        key += (BLOCK_SIZE - length) * b"}"

    iv = get_random_bytes(AES.block_size)
    encobj = AES.new(key, AES.MODE_CFB, iv)
    return iv + encobj.encrypt(data)


def decrypt_pycryptodomex(data, key):
    length = len(key)
    if length > BLOCK_SIZE:
        key = key[: -(length - BLOCK_SIZE)]
    if length not in (16, 24, 32):
        key += (BLOCK_SIZE - length) * b"}"

    iv = data[: AES.block_size]
    data = data[AES.block_size :]

    # Don't fail on decrypt
    try:
        encobj = AES.new(key, AES.MODE_CFB, iv)
        return encobj.decrypt(data)
    except Exception:
        return None


def encrypt_tinyaes(data, key):
    if len(key) > BLOCK_SIZE:
        key = key[:BLOCK_SIZE]
    else:
        key = key.zfill(BLOCK_SIZE)

    iv = os.urandom(BLOCK_SIZE)
    encobj = tinyaes.AES(key, iv)
    return iv + encobj.CTR_xcrypt_buffer(data)


def decrypt_tinyaes(data, key):
    if len(key) > BLOCK_SIZE:
        key = key[:BLOCK_SIZE]
    else:
        key = key.zfill(BLOCK_SIZE)

    iv, data = data[:BLOCK_SIZE], data[BLOCK_SIZE:]

    # Don't fail on decrypt
    try:
        res: bytes = tinyaes.AES(key, iv).CTR_xcrypt_buffer(data)
    except Exception:
        return None
    else:
        return res


data = b"foo"
key = b"secret"

# PyCryptodomex
encrypted_p = encrypt_pycryptodomex(data, key)
decrypted_p = decrypt_pycryptodomex(encrypted_p, key)
assert decrypted_p == data

# TinyAES
encrypted_t = encrypt_tinyaes(data, key)
decrypted_t = decrypt_tinyaes(encrypted_t, key)
assert decrypted_t == data

# PyCryptodomex -> TinyAES
encrypted_p = encrypt_pycryptodomex(data, key)
decrypted_t = decrypt_tinyaes(encrypted_p, key)
assert decrypted_t == data, decrypted_t
