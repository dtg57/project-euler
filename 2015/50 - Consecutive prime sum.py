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

def checkifprime(testing_number,divisors):
    if testing_number<0 or testing_number==1 or checkifodd(testing_number)==False or testing_number==4 or testing_number==6:
        return False
    if testing_number==2 or testing_number==3 or testing_number==5 or testing_number==7:
        return True
    elif testing_number!=1 or testing_number!=2 or testing_number!=3 or testing_number!=4 or testing_number!=5 or testing_number!=6 or testing_number!=7 or checkifodd(testing_number)==True:
        #divisors=listofdivisors(testing_number)
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

def listofprimes(end):
    primes=[]
    check=0
    i=0
    while True:
        if i>end:
            break
        if i>check+1000:
            print(i)
            check=i
        if checkifprime(i,listofdivisors(i)):
            primes.append(i)
        i+=1
    return primes

def sumlist(lis):
    s=0
    for i in lis:
        s+=i
    return s

def gethighest(under):
    primes=listofprimes(under/10)
    pos=0
    solutions=[]
    divisors=listofdivisors(under)
    for prime in primes:
        if pos%10==0:
            print(pos)
        for endpos in range(1,600):
            temp=primes[pos:endpos+pos]
            s=sumlist(temp)
            if s>under or len(temp)<393:
                continue
            #print(temp)
            if checkifprime(s,divisors):
                solutions.append([s,len(temp),temp])
        pos+=1
    mx,num=0,0
    for i in solutions:
        if i[1]>mx:
            mx=i[1]
            num=i[0]
    return mx,num

#print(checkifprime(sumlist([7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]),listofdivisors(1000)))
print(gethighest(1000000))
#print(listofprimes(100))
