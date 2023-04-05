import Prime_Factoriser as pFact
import math

primes = {}
cands1 = []
cands2= []
squares = []

n = 10**8


#METHOD 1: find all primes below n and, for each, prime factorise p - 1 and check if no duplicates
for i in range(3, n, 4):
    if pFact.isPrime(i)[0]:
        pfactors = pFact.primeFactorise(i - 1)
        if len(pfactors) == len(set(pfactors)):
            cands1.append(i - 1)
    if (i-3)%100000 == 0:print(i)


#METHOD 2: check each number 2, 6, 10, ... up to n (i.e. multiples of 2 but not 4) for n + 1 being prime AND for prime square divisors up to k^2 (3^2, 5^2, 7^2 ..., k^2)
'''

k = math.floor(math.sqrt(n/2))
lim = 200

primesquares = []
for j in range(3, k+1):
    if pFact.isPrime(j)[0]:
        primesquares.append(j**2)

for i in range(2, n, 4):
    if (i-2)%100000 == 0:print(i)
    if not pFact.isPrime(i+1)[0]:
        continue
    result = True
    for j in range(lim):
        psquare = primesquares[j]
        if psquare > i:
            break
        if i % psquare == 0:
            result = False
            break
    if result:
        cands2.append(i)

cands3 = []

for cand in cands2:
    result = True
    for i in range(lim, len(primesquares)):
        psquare = primesquares[i]
        #print(psquare, ' ', i)
        if psquare > cand:
            break
        if cand % psquare == 0:
            result = False
            break
    if result:
        cands3.append(cand)
        
    
def nonintersect(a, b):
    non = []
    for i in a:
        if not i in b:
            non.append(i)
    return non

'''
