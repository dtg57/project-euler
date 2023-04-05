# Problem 188: The hyperexponentiation of a number
# Solved: 21/12/2020
# Runtime: 00:11

import math

n = 1777
k = 1855
mod = 12500000
period = 312500


modtable = {}
last8 = {}
p = 1

for i in range(1,period+1):
    if i%100000 == 0:
        print(i)
    p = (p*n) % mod
    modtable[i] = p

p = 1
for i in range(1,mod):
    if i%100000 == 0:
        print(i)
    p = p*n % 10**9
    last8[i] = p

j = 1777

for i in range(k - 2):
    j = modtable[j % period]

print(last8[j%mod]%(10**8))
