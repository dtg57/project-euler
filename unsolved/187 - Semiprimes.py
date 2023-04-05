import math

class primetest:
    def __init__(self):
        self.divisors=[2, 3, 5]
        
    def isprime(self, n):
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
twopf = []
PT = primetest()
primes = []
for i in range(1, 5000000, 2):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        continue
    if i % 10001 == 0:
        print(i)
    if PT.isprime(i):
        primes.append(i)
'''
apos = 0
for a in primes:
    if apos % 1 == 0:
        print(apos)
    for b in primes:
        n = a * b
        if n >= 10 ** 8:
            continue
        else:
            twopf.append(n)
    apos += 1
print(len(n))
        
'''
count = 0
for i in range(1, 10 ** 8):
    if i % 100 == 0:
        print(i)
    for prime in primes:
        if i/prime in primes:
            count += 1
            print(i)
            break
print(count)
