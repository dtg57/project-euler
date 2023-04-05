import math
    
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
    pos=round(lowerthan)
    primes=[]
    while pos>higherthan:
        if checkifprime(pos)==True:
            primes.append(pos)
        pos=pos-1
    return primes

def getnextpf(num):
    if num%19==0:
        return num/19,19
    if num%17==0:
        return num/17,17
    if num%13==0:
        return num/13,13
    if num%11==0:
        return num/11,11
    if num%7==0:
        return num/7,7
    if num%5==0:
        return num/5,5
    if num%3==0:
        return num/3,3
    if num%2==0:
        return num/2,2
    primes=sorted(listofprimes(num/2,21))
    pos=0
    check=0
    while check<1:
        if num%primes[pos]==0:
            return num/primes[pos],primes[pos]
            check=1
        pos=pos+1

def getallpf(num):
    primefactors=[]
    if num==1:
        return []
    if checkifprime(num):
        primefactors.append(int(num))
        return primefactors
    test=num
    while checkifprime(test)==False:
        test,a=getnextpf(test)
        primefactors.append(int(a))
    primefactors.append(int(test))
    return sorted(primefactors)

#while True:   
#    print (getallpf(int(input('What number would you like to prime factorise?'))))
print (getallpf(1147))       
        

