from Crypto.Util.number import *
from tqdm import tqdm

r = exec(open("output.txt", "r").read())
BITS = 512

# brute 10 bit
rand = round(n.bit_length()/BITS)
temp = (n >> (BITS*(rand-1)+10)) << 10

for i in tqdm(range(1<<10)):
    try:
        guess_high = temp + i
        guess_phi = guess_high*pow(2,512*(rand-1))+phi
        d = inverse(e, guess_phi)
        m = long_to_bytes(pow(ct,d,n))
        if b"LKS" in m:
            print(m)
            break
    except: 
        continue
    