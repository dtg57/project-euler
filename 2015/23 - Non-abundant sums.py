import math

def properfactors(number):
    num=int(number)
    factors=[]
    sqrt=math.sqrt(float(num))
    if round(sqrt)>sqrt:
        start=round(sqrt)-1
    if round(sqrt)<sqrt:
        start=round(sqrt)
    if round(sqrt)==sqrt:
        start=sqrt
    it=int(start)
    for i in range(it-1):
        if num%start==0:
            factors.append(int(start))
            factors.append(int(num/start))
        start=start-1
    if len(factors)>1 and factors[0]==factors[1]:
        del factors[0]
    factors.append(1)
    return factors

def checkabundant(num):
    factors=properfactors(num)
    sumfactors=0
    for factor in factors:
        sumfactors=sumfactors+factor
    if sumfactors>num:
        return True
    else:
        return False

abundants=[]
for i in range(1,28124):
    if checkabundant(i):
        abundants.append(i)

def testifsum(num):
    pos1=0
    pos2=0
    tests=[]
    for i in abundants:
        if i>(num-12):
            break
        if int(num-i) in abundants:
            tests.append(True)
            nums=[i,num-i]
            break
        else:
            tests.append(False)
    if True in tests:
        return True
    else:
        return False

sums=0
for i in range(28214):
    if testifsum(i)==False:
        print (i)
        sums=sums+i
print (sums)
    
            
    
    
