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
checkifprime=primetest()

def getdiags(size):
    return [size**2,size**2-size+1,size**2-2*size+2,size**2-3*size+3]

def countprimes(diags):
    count=0
    for i in diags:
        if checkifprime.isprime(i):
            count+=1
    return count

def getfirstbelow(below):
    diags=[1,3,5,7,9]
    size=3
    count=countprimes(diags)
    poss=((size+1)/2)*4-3
    percentprime=1000*(count/poss)
    size=5
    while percentprime>=below:
        if (size-1)%1000==0:
            print(size,percentprime,count)
        new=getdiags(size)
        diags+=new
        count+=countprimes(new)
        percentprime=100*(count/poss)
        size+=2
        poss=((size+1)/2)*4-3
    return size-2
print(getfirstbelow(9))

