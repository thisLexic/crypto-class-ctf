
## Challenge Name
Sussy Curve

## Description
There is an encrypted file: flag.pdf.enc.
I had to decrypt it by identifying the key in the following code:
```python
p = 3548190181
E = EllipticCurve(GF(p), [0, 0])

P = (18435, 454929829)
Q = (1254695067, 2137017680)  # Q == d*P

key = SHA256(str(d))
```

## Insight
The only hard part in the problem is the following:
```python
E = EllipticCurve(GF(p), [0, 0])
```
I did not understand elliptic curves enough and so I kept wondering why this section of the code kept bugging out. I then realized it was because when a and b are both 0, the equation simply becomes y<sup>2</sup> = x<sup>3</sup>.

## Solution
My first step was to copy and paste the following to my code editor:
```python
p = 3548190181
E = EllipticCurve(GF(p), [0, 0])

P = (18435, 454929829)
Q = (1254695067, 2137017680)  # Q == d*P
```
Since I realized that the second line of code that kept bugging was useless, I simply removed it and I was left with the following:
```python
p = 3548190181

P = (18435, 454929829)
Q = (1254695067, 2137017680)  # Q == d*P
```
I then wanted to make sure that the section I removed actually didn't matter and the formula was really y<sup>2</sup> = x<sup>3</sup>:
```python
print("P")
print("LHS " + str((P[1]**2)%p))
print("RHS " + str((P[0]**3)%p))

print("Q")
print("LHS " + str((Q[1]**2)%p))
print("RHS " + str((Q[0]**3)%p))
```
It is in fact still correct:
```
P
LHS 2564793410
RHS 2564793410

Q
LHS 946044702
RHS 946044702
```
I then needed to find d since Q and P are already given. Moreover, the equation is right. I found d through brute-force:
```python
d = 1
while True:
    if Q == mul(P, d):
        print("d: " + str(d)) # d: 42069
        break
    d += 1
```
After finding d, it had to be hashed using sha256 (description said to do this):
```python
key = hashlib.sha256(str(d).encode('utf-8')).digest()
```
Lastly, once the key was identified, I just had to decrypt the encrypted pdf file using the key and the function that was already given for decrypting:
```python
with open("./flag.pdf.enc", "rb") as file:
    s = file.read()
    decrypted_string = decrypt(s, key)
    decfile = open(f'./flag.pdf', 'wb')
    decfile.write(decrypted_string)
    decfile.close()
```
Afterwards, I just opened the decrypted pdf file and read the flag
## Final Answer
CSCI_184.03_CTF{s1ngul4r_curv3s_r_pr3tty_5u5}
