import math

def addall(lis):
    a=0
    for i in range(len(lis)):
        a=a+int(lis[i])
    return a

def sumproperfactors(number):
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
            factors.append(start)
            factors.append(num/start)
        start=start-1
    if len(factors)>1:
        if factors[0]==factors[1]:
            del factors[0]
    factors.append(1)
    return addall(factors)

def testamicable(num):
    if num==sumproperfactors(sumproperfactors(num)) and num!=sumproperfactors(num):
        return num
    
       
amicables=[]
for i in range(1,10000):
    if testamicable(i)!=None:
        amicables.append(testamicable(i))
print (addall(amicables))
    
