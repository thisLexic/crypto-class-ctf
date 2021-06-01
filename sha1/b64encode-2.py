from binascii import hexlify, unhexlify
from base64 import b64decode, b64encode
from hashlib import sha1

MAX_LEN = 200000

with open("./messageA", "rb") as file:
    encoded_string_1 = b64encode(file.read())

with open("./messageB", "rb") as file:
    encoded_string_2 = b64encode(file.read())

# encoded_string_1 = "mQQNBH/oF4ABIAD/S2V5IGlzIHBhcnQgb2YgYSBjb2xsaXNpb24hIEl0J3MgYSB0cmFwIXnGGvCvzAVFFdknTnMHYksdx/sjmIu43otXXbp7nqsxwWdLbZdDeKgncy/1hRx2ouYHcrWkfOHqxAu5k8EtjHDiSk+NX83twbMsnPGeMa8kKXWdQuTf2zFxn1h2I+5VKTm23NxFn8pTVTtw+H7eMKJH6jr2x1mi8gsyDXYNtk/0eQhP08yzzdSDYtlqnEMGF8r/bDbGN+U/3ihBf2Jv7FTteUOkbl9XMPK7OPsd9uAJABDQDiSteL+SZBmTYI6NFYp4nzTEb+HmAn81pMv7gnB2xQ7KDot8ymm7LCt5Aln5v5Vw3Y1EN6MRX6/3w8rAmtJSZgVcJxBHVReOrv+CWiyqKs+13mTOdkHcWaVBqfycdWdW4uI9xxPIwkyXkKprDjin9V8URSocooUN3ZVi/ZoYrUJJaqlwCPdGcvaO9GHriLCZM9YmtPkYdJzAJ/3dbEJfxCFoNdATTRUoW6sst4Sk98u0+1FNS/D2I3zwCp6fEyuaBm5v0X9sQph0eFhv9lGvlnR/tCa5hyuaiOQGP1m7M0zABlD4OoDEJ1G3GXTTAPwoGaLo8eMsG1HLGOa/xNubrvZ11Kr1sVdKBH+PbdLsFTqTQSKTl02Sj4jO2TY8/vl84udCvzTJa47zh1Z2/qXMqOX33qC6skE9TeAO5x7gHxYr220er9kl5q66rmo1TvF88gWkBPvbEvxFTUH92VzyRZZkoq0DLR2mCnMmQHXX8eDWwUA656DYYd8/5XBxiN1eB9FYm5+LZjBVP4/DUrPgwn2oC926TGQCDQ=="
# encoded_string_2 = "mQMNBH/oF4ABGAD/UHJhY3RpY2FsIFNIQS0xIGNob3Nlbi1wcmVmaXggY29sbGlzaW9uIR0nbGumYeEEDh99dn8HYkndx/szLIu4wrdXXb7Hnqsr4WdLfbNDeLTLcy/hiRx2oCYHcqUQfOH26Au5l30tjGhSSk+dX83tzQssnOGSMa8m6XWdUlDf2y1Nn1hyn+5VMxm23Mxhn8pPuTtw7HLeMKCH6jrmc1mi7icyDXKxtk/syQhPw8yzzdg7Ytl6kEMGFQr/bCZyN+Uj4ihBe95v7E7NeUO0Sl9XLB67OO8R9uALwBDQHpCteKO+ZBmX3I6NDTp4nyTEb+Hqun81tMf7gnK2xQ7auot81lW7LC/FAlnjn5VwzalEN7/9X6/jz8rAmBJSZhXoJxBbeReOqkOCWjQaKs+l3mTOevncWbVNqfyetWdW8lY9xw/0wkyTLKprFBin9U8wRSoAToUNyZli/ZjYrUJZ3qlwFNtGcvIy9GHzOLCZI9YmtPWgdJzQK/3dboJfxDHcNdAPcRUoXxcst56E98uk31FNVxz2I2j8Cp6d0yuaFtpv0WNAQphwxFhv7uGvlmR/tCa1PyuamOgGP1t7M0zQslD4JrzEJ1ULGXTJIPwoCYbo8f/AG1HfFOa/xhubrubB1KrpnVdKAMOPbcpcFTqDQSKTm/WSj5jC2TY+Pvl88lNCvyj1a473O1Z25IXMqPXT3qCmXkE9WewO5xwgHxY7b20es/Ul5qoGrmot/vF84gWkBPdjEvxVQUH925zyRYbQoq0fER2mDs8mQG/38eDG5UA6+0zYYcsz5XBzSN1eF2VYm4OnZjBRg4/DSgPgwm2oC9229GQCHQ=="

username = b64decode(encoded_string_1)
password = b64decode(encoded_string_2)

# if len(username) > MAX_LEN or len(password) > MAX_LEN:
#     print("error")
if username == password:
    print("error")
elif sha1(username).digest() == sha1(password).digest():
    # print(str(encoded_string_2))
    print("nice")
    print(username, file=open("decoded-1.txt", "w"), end="")
    print(password, file=open("decoded-2.txt", "w"), end="")
    # print(encoded_string_1.decode(), file=open("shattered-1.txt", "w"), end="")
    # print(encoded_string_2.decode(), file=open("shattered-2.txt", "w"), end="")
    # print(sha1(username).digest())
    # print(sha1(password).digest())
else:
    print("error")