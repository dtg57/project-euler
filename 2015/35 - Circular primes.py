import math

def getrotations(num):
    string=str(num)
    rotations=[]
    for b in range(len(string)-1):
        i=b+1
        rotations.append(int(string[i:]+string[:i]))
    if len(string)!=1:
        rotations.append(num)
    return rotations

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
    check=lowerthan
    while pos>higherthan:
        if pos%2==1 and pos%3!=0:
            if checkifprime(pos)==True:
                primes.append(pos)
                if pos<(check-10000):
                    print (check)
                    check=pos
        pos=pos-1
    return primes

primes=listofprimes(1000000,1)
circulars=[]
for prime in primes:
    test=[]
    print (prime)
    for i in getrotations(prime):
        test.append(checkifprime(i))
    if False not in test:
        circulars.append(prime)
print (len(circulars))
