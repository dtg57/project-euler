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
    if testing_number==1 or testing_number<0 or checkifodd(testing_number)==False or testing_number==4 or testing_number==6:
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

def checkquad(a,b):
    tests=[True]
    n=0
    while tests[-1]==True:
        tests.append(checkifprime(int(n**2+a*n+b)))
        n=n+1
    return len(tests)-1

mx=[0,0,0]
for a in range(-999,1000):
    for b in range(-999,1000):
        if b%500==0: print(a,b)
        if checkquad(a,b)>mx[0]:
            mx=[checkquad(a,b),a,b]
            print (mx)
print (mx[1]*mx[2])
        
