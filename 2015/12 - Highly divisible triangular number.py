import math

def triangularnumber(pos):
    return (pos*(pos+1))/2

def findfactors(number):
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
    for i in range(it):
        if num%start==0:
            factors.append(start)
            factors.append(num/start)
        start=start-1
    return factors

i=1
while True:
    print (len(findfactors(triangularnumber(i))))
    if len(findfactors(triangularnumber(i)))>500:
        print ("I've found it!!!",i,"(",triangularnumber(i),")")
        break
    i=i+1
