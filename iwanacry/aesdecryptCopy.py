from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from secrets import token_bytes
from os import listdir

# key = token_bytes(16)
key = b'r\x86\xd2\xde\xa2U#~\xb37B\xa4\x12\xb6\xbe\xe8'
print(key)
# iv = int.from_bytes(token_bytes(16), byteorder='big') 
iv = 132382609054739350474280508136255107837
print(iv)

filename = "./test.txt.enc"

data = open(filename, 'rb').read()
print(data)
nonce = int.to_bytes(iv, 16, byteorder='big')
print(nonce)
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
aes_dec = cipher.decryptor()
txt = aes_dec.update(data) + aes_dec.finalize()

print(txt)