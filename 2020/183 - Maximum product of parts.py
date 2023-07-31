# Problem 183: Maximum product of parts
# Solved: 14/12/2020
# Runtime: 00:01

import math
from prime_test_factorise import primeFactorise

def prodlist(l):
    if len(l) == 0:
        return 1
    p = 1
    for el in l:
        p *= el
    return p

def logp(N, k):
    return k*math.log(N/k)

powers2 = []
powers5 = []
terminatingd = [1]

for i in range(0, 14):
    powers2.append(2**i)
for i in range(0, 6):
    powers5.append(5**i)

for i in powers2:
    for j in powers5:
        prod = i * j
        if prod < 10**4 and prod != 1:
            terminatingd.append(prod)

s=0
for N in range(5, 10001):
    kbelow = math.floor(N/math.e)
    kabove = math.ceil(N/math.e)
    pbelow = logp(N, kbelow)
    pabove = logp(N, kabove)
    pbest = N/kbelow if pbelow > pabove else N/kabove
    terminating = False
    for d in terminatingd:
        if (d * pbest % 1) < 0.000000001:
            terminating = True
            break
    if (N%100 == 0):
        print(N,' ', terminating, ' ', pbest)
    if terminating:
        s -= N
    else:
        s += N

print(s)
