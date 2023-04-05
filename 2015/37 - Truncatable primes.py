import math
    
def checkifodd(num):
    number=int(num)
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
    if testing_number==1 or checkifodd(testing_number)==False or testing_number==4 or testing_number==6:
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

def listofprimes(lowerthan,higherthan):
    pos=lowerthan
    primes=[]
    while pos>higherthan:
        if checkifprime(pos)==True:
            primes.append(pos)
        pos=pos-1
    return primes

def tptest(num):
    truncs=[]
    string=str(num)
    for i in range(1,len(string)+2):
        truncs.append(string[0:i])
    for i in range(0,len(string)+1):
        truncs.append(string[i:len(string)+2])
    del truncs[-1]
    test=[]
    for number in truncs:
        test.append(checkifprime(int(number)))
    if False in test:
        return False
    else:
        return True

primes=listofprimes(100000,10)
tprimes=[]
s=0
for prime in primes:
    print (prime)
    if tptest(prime)==True:
        tprimes.append(prime)
        s=s+prime
print (tprimes,s)


