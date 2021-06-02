#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from secrets import token_bytes
from os import listdir

key = token_bytes(16)
print("key: " + str(key))
iv = int.from_bytes(token_bytes(16), byteorder='big')
print("iv: " + str(iv))

for filename in ["./test.txt"]:
    # print(f'Encrypting {filename}')
    data = open(filename, 'rb').read()
    print("data: " + str(data))

    nonce = int.to_bytes(iv, 16, byteorder='big')
    print("nonce: " + str(nonce))
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    # print("cipher: " + str(cipher))
    aes_enc = cipher.encryptor()
    # print("aes_enc: " + str(aes_enc))
    ctxt = aes_enc.update(data) + aes_enc.finalize()
    # print("aes_enc finalized: " + str(aes_enc))
    print("ctxt: " + str(ctxt))
    
    encfile = open(f'{filename}.enc', 'wb')
    encfile.write(ctxt)
    encfile.close()

    iv += 1
