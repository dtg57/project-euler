def checkpandig(string):
    digits=[]
    for i in range(1,len(string)+1):
        digits.append(str(i))
    test=[]
    for digit in digits:
        if digit in string:test.append(True)
        else:
            test.append(False)
            break
    if False in test:return False
    else:return True
products=[]
for a in range(1,10000):
    for b in range(1,10000):
        if b%1000==0:print(a,b)
        if len(str(a))+len(str(b))+len(str(a*b))==9:
            if checkpandig(str(a)+str(b)+str(a*b)):
                products.append(a*b)
total=0           
for i in set(products):total=total+i
print (total)
                
