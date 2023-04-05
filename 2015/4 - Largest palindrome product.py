import math

    
def listify(string):
    a=[]
    pos=0
    for i in range(len(string)):
        a.append(string[pos])
        pos=pos+1
    return a
def checkpalindrome(num):
    testing=listify(str(num))
    if len(testing)%2==0:
        times=int(len(testing)/2)
    if len(testing)%2==1:
        times=int((len(testing)/2)-0.5)
    iterations=0
    check=[]
    for i in range(times):
        a=testing[iterations]
        b=testing[((-iterations)-1)]
        if a==b:
            check.append(1)
        if a!=b:
            check.append(0)
        iterations=iterations+1
    if 0 in check:
        return False
    if 0 not in check:
        return True

a=999
b=999
bignums=[]
for i in range(100):
    a=999
    for i in range(100):
        bignums.append([a,b,a*b])
        a=a-1
    b=b-1


def checkmany(test):
    checklist=[]
    item=0
    for i in range(len(test)):
        if checkpalindrome(test[item][2])==True:
            checklist.append(test[item])
        item=item+1
    return checklist
print (checkmany(bignums))

        




