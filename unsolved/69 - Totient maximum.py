import math

class primetest:
    def __init__(self):
        self.divisors = [2, 3, 5]
        
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

divs = {}
hcftried = {}

def hcf(num1, num2):
    global hcftried
    no1 = num1
    no2 = num2
    if (no1, no2) in hcftried:
        return hcftried[(no1, no2)]
    if (no2, no1) in hcftried:
        return hcftried[(no2, no1)]
    while no1 != no2:  
        if no1 > no2:  
            no1 -= no2  
        elif no2 > no1:  
            no2 -= no1
    hcftried = addmany(num1, num2, no1)
    return no1
    
def isdiv(divisors, num, divisor):
    if num in divisors:
        if divisor in divisors[num]:
            return True
        else:
            return False
    return False
    
def numoffacts(num):
    count=2
    if (num/3)%1!=0 or (num/5)%1!=0 or (num/7)%1!=0:
        return 2
    for i in range(2,math.floor(num**0.5)+1):
        div=num/i
        if div%1!=0:
            continue
        elif div==i:
            count+=1
        elif div%1==0:
            count+=2
    return count

def addmany(num1, num2, gcd):
    global hcftried
    a=num1
    b=num2
    while a < 1000000:
        hcftried[(a, num2)] = gcd
        a += a
    while b < 1000000:
        hcftried[(num1, b)] = gcd
        b += a
    return hcftried

def addmanydivs(div, num, divs):
    def adddiv(div, num, divs):
        if num in divs:
            divs[num].append(div)
        else:
            divs[num] = [div]
        return divs
    while num < 1000000:
        divs = adddiv(div, num, divs)
        num += num
    return divs
        
def totient(num):
    global divs
    global hcftried
    mod2 = num%2 == 0
    mod3 = num%3 == 0
    mod5 = num%5 == 0
    count=1
    for i in range(2, num+1):
        if (i%2 == 0 and mod2) or (i%3 == 0 and mod3) or (i%5 == 0 and mod5):
            continue
        if isdiv(divs, num, i):
            continue
        gcd = hcf(num, i)
        if gcd == 1:
            count+=1
        else:
            divs = addmanydivs(i, num, divs)
    return count

def checkvalid(num, ptest):
    if ptest.isprime(i):
        return False
    facts = numoffacts(num)
    if facts/i < 0.00011:
        return False
    return True
    
mx=4.8125
checkprime=primetest()

for i in range(3000,1000000,2):
    if i%100==0:
        print(i)
    if not checkvalid(i, checkprime):
        continue
    t=i/totient(i)
    if t>mx:
        mx=t
        print('new max:',mx,i,facts)
print(mx)
#print(numoffacts(7000))
#while True:
#    print(totient(int(input('Number?'))))
