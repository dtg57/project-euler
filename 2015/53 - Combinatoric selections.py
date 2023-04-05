import math
def getlist():
    lis=[]
    for n in range(1,101):
        for r in range(1,101):
            if r<n: lis.append([r,n])
    return lis
def checkcom(select,fromm): return((math.factorial(fromm))/(math.factorial(select)*math.factorial(fromm-select)))
sels=0
lis=getlist()
for item in lis:
    if checkcom(item[0],item[1])>1000000:sels=sels+1
print (sels)
