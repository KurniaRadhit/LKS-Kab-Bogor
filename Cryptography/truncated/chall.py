from Crypto.Util.number import *
from Crypto.Random import random

FLAG = b"LKS{REDACTED}"
BITS = 512

rand = random.randint(2,10)
primes = [getPrime(BITS) for _ in range(rand)]
e = 0x10001
n = phi = 1
for i in range(rand):
    n *= primes[i]
    phi *= primes[i]-1
d = inverse(e,phi)
c = pow(bytes_to_long(FLAG), e, n)

print("n = ", n)
print("e = ", e)
print("ct = ", c)
print("phi = ", phi&((1<<(BITS*(rand-1)))-1))
