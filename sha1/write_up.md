  

## Challenge Name
Shattered

  

## Description
TLDR - login to the admin portal in bfwadmin.lunchtimeattack.wtf.

The Better Freedom Wall admins have made "significant progress," whatever that means! You just found out that they have a super secret admin portal: bfwadmin.lunchtimeattack.wtf

Your friend also managed to yoink the server code that runs it.

The admin portal has a login page and you have to enter a right username and password to get in.

## Insight
The server code had a really important section:
```python
sha1(username).digest() == sha1(password).digest()
	return FLAG
```

This meant that all I had to do was enter a string A and a string B that had the same hash when put through sha1.

  

## Solution
Upon realizing that all I needed was two strings that had the same hash when put through sha1, I just googled "sha1 collision text sample." I coulnd't simply use the same text values since there is the following if statement:

```python
if len(username) > MAX_LEN or len(password) > MAX_LEN:
	return jsonify({'error': 'Request is too large.'})
```

At this point I saw the following messageA and messageB that had the same sha1 from the following website: https://sha-mbles.github.io/.

I then confirmed that they had the same sha1 through the command line:

```linux
sha1sum message*
```

This resulted to the following that did in fact confirm they have the same hash for sha1:
```linux
8ac60ba76f1999a1ab70223f225aefdc78d4ddc0 messageA
8ac60ba76f1999a1ab70223f225aefdc78d4ddc0 messageB
```

This server code made me realize that I needed to upload the file encoded in base 64:
```python
username = b64decode(request.form['user'])
password = b64decode(request.form['pass'])
```
That is why I encoded the file in base 64 through this method:
```python
with open("./messageA", "rb") as file:
	encoded_string_1 = b64encode(file.read())
with open("./messageB", "rb") as file:
	encoded_string_2 = b64encode(file.read())
```

At this point, both encoded strings are binary strings. What I needed was just strings. That is why I printed both encoded strings into the console. I then copied both outputs making sure I did not include the "b" or the " ' " when I did so. I then pasted these values and hard coded it through the following:

```python
encoded_string_1 = "mQQNBH/oF4ABIAD/S2V5IGlzIHBhcnQgb2YgYSBjb2xsaXNpb24hIEl0J3MgYSB0cmFwIXnGGvCvzAVFFdknTnMHYksdx/sjmIu43otXXbp7nqsxwWdLbZdDeKgncy/1hRx2ouYHcrWkfOHqxAu5k8EtjHDiSk+NX83twbMsnPGeMa8kKXWdQuTf2zFxn1h2I+5VKTm23NxFn8pTVTtw+H7eMKJH6jr2x1mi8gsyDXYNtk/0eQhP08yzzdSDYtlqnEMGF8r/bDbGN+U/3ihBf2Jv7FTteUOkbl9XMPK7OPsd9uAJABDQDiSteL+SZBmTYI6NFYp4nzTEb+HmAn81pMv7gnB2xQ7KDot8ymm7LCt5Aln5v5Vw3Y1EN6MRX6/3w8rAmtJSZgVcJxBHVReOrv+CWiyqKs+13mTOdkHcWaVBqfycdWdW4uI9xxPIwkyXkKprDjin9V8URSocooUN3ZVi/ZoYrUJJaqlwCPdGcvaO9GHriLCZM9YmtPkYdJzAJ/3dbEJfxCFoNdATTRUoW6sst4Sk98u0+1FNS/D2I3zwCp6fEyuaBm5v0X9sQph0eFhv9lGvlnR/tCa5hyuaiOQGP1m7M0zABlD4OoDEJ1G3GXTTAPwoGaLo8eMsG1HLGOa/xNubrvZ11Kr1sVdKBH+PbdLsFTqTQSKTl02Sj4jO2TY8/vl84udCvzTJa47zh1Z2/qXMqOX33qC6skE9TeAO5x7gHxYr220er9kl5q66rmo1TvF88gWkBPvbEvxFTUH92VzyRZZkoq0DLR2mCnMmQHXX8eDWwUA656DYYd8/5XBxiN1eB9FYm5+LZjBVP4/DUrPgwn2oC926TGQCDQ=="
encoded_string_2 = "mQMNBH/oF4ABGAD/UHJhY3RpY2FsIFNIQS0xIGNob3Nlbi1wcmVmaXggY29sbGlzaW9uIR0nbGumYeEEDh99dn8HYkndx/szLIu4wrdXXb7Hnqsr4WdLfbNDeLTLcy/hiRx2oCYHcqUQfOH26Au5l30tjGhSSk+dX83tzQssnOGSMa8m6XWdUlDf2y1Nn1hyn+5VMxm23Mxhn8pPuTtw7HLeMKCH6jrmc1mi7icyDXKxtk/syQhPw8yzzdg7Ytl6kEMGFQr/bCZyN+Uj4ihBe95v7E7NeUO0Sl9XLB67OO8R9uALwBDQHpCteKO+ZBmX3I6NDTp4nyTEb+Hqun81tMf7gnK2xQ7auot81lW7LC/FAlnjn5VwzalEN7/9X6/jz8rAmBJSZhXoJxBbeReOqkOCWjQaKs+l3mTOevncWbVNqfyetWdW8lY9xw/0wkyTLKprFBin9U8wRSoAToUNyZli/ZjYrUJZ3qlwFNtGcvIy9GHzOLCZI9YmtPWgdJzQK/3dboJfxDHcNdAPcRUoXxcst56E98uk31FNVxz2I2j8Cp6d0yuaFtpv0WNAQphwxFhv7uGvlmR/tCa1PyuamOgGP1t7M0zQslD4JrzEJ1ULGXTJIPwoCYbo8f/AG1HfFOa/xhubrubB1KrpnVdKAMOPbcpcFTqDQSKTm/WSj5jC2TY+Pvl88lNCvyj1a473O1Z25IXMqPXT3qCmXkE9WewO5xwgHxY7b20es/Ul5qoGrmot/vF84gWkBPdjEvxVQUH925zyRYbQoq0fER2mDs8mQG/38eDG5UA6+0zYYcsz5XBzSN1eF2VYm4OnZjBRg4/DSgPgwm2oC9229GQCHQ=="
```

I then needed to upload the values to the server through the following way:

```python
r = requests.post('http://bfwadmin.lunchtimeattack.wtf/login', data={'user' :encoded_string_1,'pass' :encoded_string_2})
```

The server then sent the flag to the command line.

  

## Final Answer

CSCI_184.03_CTF{7h3_SHA_1n_sha-1_57and5_4_SHAtt3r3d!!!}
