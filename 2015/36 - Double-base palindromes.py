def checkpalindrome(num):
    testing=list(str(num))
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

total=0
for i in range(1000000):
    if checkpalindrome(i)==True and checkpalindrome(int(bin(i)[2:]))==True: total=total+i
print (total)
#print ((bin(585))[2:])
