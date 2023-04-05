import math
'''def divisors(n):
    c = 0
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                c -= 1
            c += 2
    return c
for i in range(1, 1000000):
    a = divisors(i)
    #print(i, divisors(i))
print('done')
'''
primesdone = {}
class primetest:
    def __init__(self):
        self.divisors=[2, 3, 5]
        
    def isprime(self, n):
        global primesdone
        if n in primesdone:
            return primesdone[n]
        if n==1:
            return False
        if n==2:
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
PT=primetest()

def primelist(below):
    primes = []
    for i in range(2, below):
        if PT.isprime(i):
            primes.append(i)
    return primes

def tau(n):
    if n == 1:
        return 0
    pfs = {}
    primes = primelist(math.floor(math.sqrt(n)) + 1)
    for i in primes:
        if PT.isprime(n):
            break
        while n % i == 0:
            if i in pfs:
                pfs[i] += 1
            else:
                pfs[i] = 1
            n = n // i
            if n % 1 != 0:
                n *= i
                break
    pfs[n] = 1
    count = 1
    for i in pfs:
        if i == 1:
            continue
        count *= pfs[i]+1
    return count
divnums = {}
for i in range(2, 10**7):
    if i % 1000 == 0:
        print(i)
    divnums[i] = tau(i)
