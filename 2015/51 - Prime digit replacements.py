import math
import itertools

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
    
checkprime=primetest()
posses1 = {}

def replacementposses(length):
    global posses1
    if length in posses1:
        return posses1[length]
    r = range(length)
    posses = []
    for i in range(1, length):
        posses += (list(itertools.combinations(r, i)))
    posses1[length] = posses
    return posses

def replacedigs(posses, num, rep):
    num = list(str(num))
    for pos in posses:
        num[pos] = str(rep)
    return int(''.join(num))

def getreplaced(num):
    reps = []
    posses = replacementposses(len(str(num)))
    for pos in posses:
        reps.append([])        
        for rep in range(10):
            now = replacedigs(pos, num, rep)
            if len(str(now)) == len(str(num)):
                if checkprime.isprime(now):
                    reps[-1].append(now)
    return reps
    
def getfamilylength(num):
    global familylens
    if num in familylens:
        return familylens[num]
    replaced = getreplaced(num)
    mx = [0, 0]
    pos = 0
    for i in replaced:
        if len(i) > mx[0]:
            mx = [len(i), pos]
        pos += 1
    end = [mx[0], replaced[mx[1]]]
    for i in end[1]:
        familylens[i] = [end[0], end[1]]
    return end

familylens = {}
eight = [0, 0]
test = 11
while eight == [0, 0]:
    if (test - 1) % 100 == 0:
        print(test)
    while not checkprime.isprime(test):
        test += 2
    family = getfamilylength(test)
    if family[0] >= 8:
        eight = [test, family[1]]
    test += 2

print(family)
