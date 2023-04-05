import math
import sys
def checkifodd(number):
    if number==2:
        return True
    if number%2==0:
        return False
    if number%1>0:
        return False
    if number%2==1:
        return True

def listofdivisors(number):
    if number==2:
        return ([])
    sqrt=float(math.sqrt(float(number)))
    start=sqrt+(1-sqrt%1)
    divisors=[]
    while True:
        divisors.append(start)
        start=start-1
        if start<2:
            break
    return divisors

def checkifprime(testing_number):
    if testing_number<0 or testing_number==1 or checkifodd(testing_number)==False or testing_number==4 or testing_number==6:
        return False
    if testing_number==2 or testing_number==3 or testing_number==5 or testing_number==7:
        return True
    elif testing_number!=1 or testing_number!=2 or testing_number!=3 or testing_number!=4 or testing_number!=5 or testing_number!=6 or testing_number!=7 or checkifodd(testing_number)==True:
        divisors=listofdivisors(testing_number)
        checklist=[]
        position=0
        for i in range(len(divisors)):
            if (testing_number/divisors[position])%1>0:
                checklist.append(0)
            elif (testing_number/divisors[position])%1==0:
                checklist.append(1)
            position=position+1
    if 1 in checklist and testing_number!=2:
        return False
    elif not 1 in checklist or testing_number==2:
        return True

def checkpermut(num1,num2):
    num1=list(str(num1))
    num2=list(str(num2))
    for i in num1:
        if i not in num2:
            return False
    for i in num2:
        if i not in num1:
            return False
    return True

primes=[]
for i in range(1000,10000):
    if checkifprime(i):
        primes.append(i)

for prime in primes:
    print(prime)
    for diff in range(2,int((10000-prime)/2),2):
        a,b=prime+diff,prime+diff*2
        if diff<10000 and a<10000 and b<10000 and checkifprime(a) and checkifprime(b):
            if checkpermut(prime,a) and checkpermut(prime,b):
                print(prime,a,b)
                #sys.exit()

