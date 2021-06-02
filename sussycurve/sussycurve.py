#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from secrets import token_bytes
from binascii import hexlify, unhexlify

p = 3548190181
A = 0
B = 0

def invmod(x):
    # secret trick by Fermat
    return pow(x, p-2, p)

def add(P, Q):
    (x1, y1), (x2, y2) = P, Q
    if x1 == x2:
        slope = (3*x1**2 + A) * invmod(2*y1)
    else:
        slope = (y2-y1) * invmod(x2-x1)
    x3 = (slope**2 - x1 - x2) % p
    y3 = (slope*(x1-x3) - y1) % p
    return (x3, y3)

def mul(P, k):
    if k == 1:
        return P
    elif k & 1:
        return add(P, mul(P, k-1))
    else:
        return mul(add(P, P), k//2)

# encrypting stuff

def pkcs7_pad(p, blklen=16):
    n = blklen - (len(p) % blklen)
    return p + bytes([n]*n)

def pkcs7_unpad(p, blklen=16):
    if not len(p) % blklen == 0:
        raise Exception
    last_byte = p[-1]
    pad = bytes([last_byte]*last_byte)
    if last_byte > blklen or last_byte < 1:
        raise Exception
    if not p.endswith(pad):
        raise Exception
    return p[:-last_byte]

def encrypt(p, k):
    iv = token_bytes(16)
    cipher = Cipher(algorithms.AES(k), modes.CBC(iv))
    aes_enc = cipher.encryptor()
    c = aes_enc.update(pkcs7_pad(p)) + aes_enc.finalize()
    return iv + c

def decrypt(c, k):
    iv = c[:16]
    cipher = Cipher(algorithms.AES(k), modes.CBC(iv))
    aes_dec = cipher.decryptor()
    p = aes_dec.update(c[16:]) + aes_dec.finalize()
    return pkcs7_unpad(p)
