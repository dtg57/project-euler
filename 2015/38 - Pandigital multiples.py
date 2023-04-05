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
def getmax(num):
    test=1
    t='0'
    while int(t)<987654321:
        t=t+str(test*num)
        test=test+1
    return test-2
def concatenate(num):
    mx=getmax(num)
    final=''
    for i in range(1,mx+1):
        final=final+str(i*num)
    return int(final)
    

mx=[0,0]
for i in range(1,5000000):
    if i%1000==0:print(i)
    if len(str(concatenate(i)))==9:
        if checkpandig(str(concatenate(i))):mx[0],mx[1]=i,getmax(i)
print (mx)
