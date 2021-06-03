
## Challenge Name
RSA Encraption

## Description

TLDR - Decrypt the flag encrypted using 256-bit **RSA encraption**. 

The following are the hints:
```python
N = 0x83cb50c5dfdf46956f3264f1d86aaa349b3e5467dd21c3378bb9b8188441f8a2030c52a0d34535b32ea7a24e9feb8b73d1e5dd7b9de49954c2973fb95cd0b5b3
e = 0x11
c = 0x7e541ac2d36e77516b6fca21c585e5eeac81c4755aefee32924c2edf58ea6be64710a054d6ec03eb5812f42ebd96fa951f726364629bf36d58cbb5c4bbc4ca10
```
These values can be used for getting the other necessary data for decrypting.

## Insight
The linked pdf file is extremely overwhelming: https://eprint.iacr.org/2020/1059.pdf. However, if you read the hint carefully, it simply states to implement Algorithm 1 and 2. In other words, just understand those two sections and decrypting would be easy. This makes the problem straightforward to answer once you realize you just need to implement the pseudocode into, in this case, python code.

## Solution
Based on the following given code:
```python
def rsa_decrapt(c, N, e, p, q):
    # to-do: implement Algs 1 and 2 from https://eprint.iacr.org/2020/1059.pdf
    raise NotImplementedError
```
I needed to find p and q to decrypt. Based on this other given code:
```python
p = random_prime(2^n-1, lbound=2^(n-1), proof=False)
q = random_prime(2^n-1, lbound=2^(n-1), proof=False)
N = p*q
```
I just needed to factor the already given N. I converted N into an integer through the following:
```python
N_must = 0x83cb50c5dfdf46956f3264f1d86aaa349b3e5467dd21c3378bb9b8188441f8a2030c52a0d34535b32ea7a24e9feb8b73d1e5dd7b9de49954c2973fb95cd0b5b3
N_must
```
This printed out the integer representation of N. The integer representation can then be put into factordb resulting in getting the values for p and q.
Thus, all the necessary components for decrypting are with me:
```python
N = 0x83cb50c5dfdf46956f3264f1d86aaa349b3e5467dd21c3378bb9b8188441f8a2030c52a0d34535b32ea7a24e9feb8b73d1e5dd7b9de49954c2973fb95cd0b5b3
e = 0x11
c = 0x7e541ac2d36e77516b6fca21c585e5eeac81c4755aefee32924c2edf58ea6be64710a054d6ec03eb5812f42ebd96fa951f726364629bf36d58cbb5c4bbc4ca10
p = 77882408867466414737830823616442124246477860244154061584419909218327446081643
q = 88628773929669161867967842327890631701867422108782526344419773382770618589657
```
Afterwards, just implement the two algorithms in https://eprint.iacr.org/2020/1059.pdf. However, in algo 2, there is no need to do the if statement anymore. This if statement checks whether x is a correctly padded plaintext. This step is unnecessary since the e is very small (17). Therefore, just go through each x and find the one that looks legible. In the code, I just kept appending x.

```python
def getge(p, q, e):
    symbol1 = ((p-1)*(q-1))/e
    g = 1
    while True:
        g += 1
        ge = mod(g,N)^symbol1
        if ge != 1:
            return ge

def rsa_decrapt(c, N, e, p, q):
    symbol1 = ((p-1)*(q-1))/e
    d = (e**-1)%symbol1
    a = mod(c,N)^d
    ge = getge(p, q, e)
    
    P = []
    l = 1%N
    for i in range(e):
        x = (a*l)%N
        P.append(x)
        l = (l*ge)%N
    return P
```
Once P is filled with all the x, print each element out using the given int_to_ascii function. We have to convert it to ascii because the given algorithm converted the ascii plain text into an integer through ```ascii_to_int(ptxt)```. Therefore, the flag must be converted into ascii:
```python
def int_to_ascii(i):
    return unhexlify(hex(i)[2:])

for x in rsa_decrapt(c, N, e, p, q):
    print(int_to_ascii(x))
```
This will print out the following:
```
b'`\xc45\x9b\x87\x13]9\x8bt\xa9\xc5\xfa7\xc8L\xb8\xf2"V\xaa\x7f1e\xb0d\xe7\x8a\x80\xdb\xd7\xd2\x15y\xd2\xef\x08o\xf7\xee\xc2\x98H$e\x00\x1b\xa0U\xfc\x8e={ea\x07\xa65bC)\xb1i\x91'
b':\x8d\xa6`\xefm)\x8a`\xe4\xd4N\xaf\xe2\xbcaP{9\x81\xca\xf3T}\x95\x17>\x03+\x1a\xd7\x81\xff\xea\\\r\x83\xbb\xbfW\x1c\xf7\xd065\xdaX\xe8"\x81\xc8\xb8\xa7\x0c\x92\x8e3\xbd\x1b\x88\x9d[m\xb4'
b'CSCI_184.03_CTF{n0_m3s5age_15_und3cr4p7abl3}'
...
```
One of them stands out. Just use that and that's the flag.


## Final Answer
CSCI_184.03_CTF{n0_m3s5age_15_und3cr4p7abl3}
