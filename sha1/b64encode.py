import base64
from hashlib import sha1

with open("./shattered-1.pdf", "rb") as pdf_file:
    encoded_string_1 = base64.b64encode(pdf_file.read()[:500])

with open("./shattered-2.pdf", "rb") as pdf_file:
    encoded_string_2 = base64.b64encode(pdf_file.read()[:500])

print(sha1(base64.b64decode(encoded_string_1)).digest() == sha1(base64.b64decode(encoded_string_2)).digest())
# print(encoded_string_1 == encoded_string_2)
# print(encoded_string_1)
# print(encoded_string_2)
# print(base64.b64decode(encoded_string_1))
# print(base64.b64decode(encoded_string_2))
print(base64.b64decode(encoded_string_1), file=open("decoded-1.txt", "w"), end="")
print(base64.b64decode(encoded_string_2), file=open("decoded-2.txt", "w"), end="")