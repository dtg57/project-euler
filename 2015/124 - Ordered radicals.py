import math

class primetest:
    def __init__(self):
        self.divisors=[2, 3, 5]
        
    def isprime(self, n):
        if n == 1:
            return False
        if n == 2:
            return True
        sqrt=math.ceil(math.sqrt(n))
        for div in self.divisors:
            if div>sqrt:
                return True
            if n%div==0:
                return False
        divcand=div
        nNewPrimeCount = 0
        while divcand<sqrt or nNewPrimeCount == 0:
            if divcand %2 == 0:
                divcand += 1
            else:
                divcand += 2
            if self.isprime(divcand):
                nNewPrimeCount += 1
                self.divisors.append(divcand)
                if n%divcand==0:
                    return False
        return True
    
PT = primetest()

def primelist(bottom, top):
    global PT
    primes = []
    for i in range(bottom, top):
        if PT.isprime(i):
            primes.append(i)
    return primes

def getpf(n):
    primes = primelist(1, int(n ** 0.5) + 1)
    prime_factors = []
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1: prime_factors.append(n)
    return list(set(prime_factors))

def rad(n):
    product = 1
    for i in getpf(n):
        product *= i
    return product

rads = []

for i in range(1, 100001):
    if i % 1000 == 0:
        print(i)
    rads.append([i, rad(i)])
rads.sort(key = lambda s: s[1])
print(rads[10000 - 1])
    
