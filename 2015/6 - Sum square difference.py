import math
x=[]
def addall(lis):
    a=0
    for item in lis:
       a=a+item
    return a
def addsquares(lis):
    a=0
    for item in lis:
        a=a+(item**2)
    return a
for i in range(1,101):
    x.append(i)
print ((addall(x)**2)-addsquares(x))
