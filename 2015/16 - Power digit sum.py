import math

def addall(lis):
    a=0
    for i in range(len(lis)):
        a=a+int(lis[i])
    return a

def addalldigits(num):
    lis=list(str(num))
    return (addall(lis))

print (addalldigits(math.factorial(100)))
