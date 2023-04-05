# Problem 479: Roots on the rise
# Solved: 20/12/2020
# Runtime: 00:10

import math

n = 1000000
mod=1000000007


def chooseMod(n, r):
    global mod
    if r > n:
        return 0
    if r ==0 or r==n:
        return 1
    if r ==1 or r == n-1:
        return n % mod
    num = 1
    for i in range(n, n-r, -1):
        num = (num*i) % mod
    denom = 1
    for i in range(1, r+1):
        denom = (denom*i) % mod
    return (num*pow(denom, mod - 2, mod)) % mod


'''s = 0

for k in range(1, n+1):
    print(k)
    temp = 0
    for j in range(n):
        temp += (-1)**j * ((chooseMod(n, j+1) * pow(k, 2*j, mod)) % mod)
        if (j%100 ==0):print(j)
    s += ((1 - k**2) * temp) % mod
''' 

s=0

for k in range(1, n+1):
    if k%10000==0:
        print(k)
    temp = 1 - k**2
    s += (pow(1 - temp, mod - 2, mod) * temp * (1 - pow(temp, n, mod))) % mod
print(s%mod)
