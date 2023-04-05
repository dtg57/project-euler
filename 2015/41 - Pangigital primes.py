import math

def checkpandig(num):
    num=str(num)
    for i in range(1,len(num)+1):
        if num.count(str(i))!=1:
            return False
    return True


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

def getplus(num):
    num=list(str(num))
    pos=0
    for i in num:
        if int(i)>len(num):
            return (10**(len(num)-pos-1))
        pos+=1
    return 0
oPT=primetest()
test=1
primes=[]
while True:
    while test%3==0 or test%5==0 or test%7==0 or test%11==0 or test%13==0:
        test+=2
    if (test-1)%10000==0:
        print (test-1)
    if oPT.isprime(test):
        if checkpandig(test):
            print('prime',test)
    test+=2+getplus(test)
print(prime)
print(checkpandig(50213497))
    
