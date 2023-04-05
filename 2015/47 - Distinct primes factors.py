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

def primesbetween(bot,top):
    primesa=[0]
    i=int(round(bot))-1
    t=int(round(top))+1
    while int(primesa[-1])<t:
        if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0:
            if checkifprime(i):
                primesa.append(i)
        i=i+1
    del primesa[0]
    return primesa

def getnextpf(num,lis):
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
    primes=sorted(lis)
    pos=0
    check=0
    while check<1:
        if num%primes[pos]==0:
            return num/primes[pos],primes[pos]
            check=1
        pos=pos+1

def getallpf(num,listp):
    primefactors=[]
    if num==1:return []
    if checkifprime(num):return[int(num)]
    test=num
    while not checkifprime(test): #and len(primefactors)<5:
        test,a=getnextpf(test,listp)
        primefactors.append(int(a))
    primefactors.append(int(test))
    return sorted(primefactors)

def testall(start):
    primes=primesbetween(21,start/19)
    prime=0
    test=start
    while prime==0:
        if test%100==0:print (test)
        if len(set(getallpf(test,primes)))==4 and len(set(getallpf(test+1,primes)))==4 and len(set(getallpf(test+2,primes)))==4 and len(set(getallpf(test+3,primes)))==4:
            prime=test
            break
        #if checkifprime(test+1): test=test+1
        test=test+1
        if primesbetween((test-1)/19,test/19)!=[]: primes.append(primesbetween((test-1)/19,test/19)[0])
    return ('Here it is:',prime)
        
print(testall(117000))


