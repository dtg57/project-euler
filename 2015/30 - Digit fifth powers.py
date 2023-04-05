def checkfifth(num):
    string=str(num)
    total=0
    for i in string:
        total=total+(int(i)**5)
    if total==num:
        return num
    else:
        return 0

sums=0
for i in range(1000,1000000):
    if i%10000==0:
        print (i)
    sums=sums+checkfifth(i)
print (sums)
        
