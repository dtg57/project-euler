numsegs = {'b':0, 0:95, 1:5, 2:118, 3:117, 4:45, 5:121, 6:123, 7:77, 8:127, 9:125}
changesdone = {}
def allchanges(num1, num2):
    def getchange(dig1, dig2):
        global changesdone
        tuple1 = (dig1, dig2)
        tuple2 = (dig2, dig1)
        if tuple1 in changesdone:
            return changesdone[tuple1]
        if tuple2 in changesdone:
            return changesdone[tuple2]
        if dig1 != 'b':
            dig1 = int(dig1)
        if dig2 != 'b':
            dig2 = int(dig2)
        global numsegs
        binchange = bin(numsegs[dig1] ^ numsegs[dig2])
        end = str(binchange).count('1')
        changesdone[tuple1] = end
        changesdone[tuple2] = end
        
        return end
    n1 = list(str(num1))
    n2 = list(str(num2))
    len1 = len(n1)
    len2 = len(n2)
    mx = max(len1, len2)
    mn = min(len1, len2)
    for i in range(mx - mn):
        if mx == len1:
            n2 = ['b'] + n2
        if mx == len2:
            n1 = ['b'] + n1
    s = 0
    for pos in range(len(n1)):
        s += getchange(n1[pos], n2[pos])
    return s

def digitalroots(n):
    def digroot(n):
        n = str(n)
        s = 0
        for i in n:
            s += int(i)
        return s
    digroots = [n]
    current = digroot(n)
    while len(str(current)) > 1:
        digroots.append(current)
        current = digroot(current)
    digroots.append(current)
    return digroots

def maxpower(n):
    s = 0
    digroots = ['b'] + digitalroots(n) + ['b']
    for i in range(len(digroots) - 1):
        s += allchanges(digroots[i], digroots[i + 1])
    return s

def sampower(n):
    digroots = digitalroots(n)
    digroots2 = ['b']
    s = 0
    for i in range(len(digroots)):
        digroots2.append(digroots[i])
        digroots2.append('b')
    for i in range(len(digroots2) - 1):
        s += allchanges(digroots2[i], digroots2[i + 1])
    return s

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
    
PT=primetest()
primes = []
for i in range(10**7 + 1, 2 * 10**7 + 1, 2):
    if (i - 1) % 100000 == 0:
        print(i)
    if PT.isprime(i):
        primes.append(i)
    
samsum = 0
maxsum = 0
for i in primes:
    samsum += sampower(i)
    maxsum += maxpower(i)
print(abs(samsum - maxsum))
    
