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
def hcf(no1,no2):  
    while no1!=no2:  
        if no1>no2:  
            no1-=no2  
        elif no2>no1:  
            no2-=no1  
    return no1
oPT=primetest()
count=0
for dem in range(2,1000001):
    if dem%1000==0:
        print(dem)
    if oPT.isprime(dem):
        count+=dem-1
    else:
        for num in range(1,dem+1):
            if num>=dem:
                break
            if dem%2==0 and num%2==0:
                continue
            if hcf(num,dem)==1:
                count+=1
print(count)
            
