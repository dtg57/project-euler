def checkdivisibility(testnum):
    b=0
    for i in range(1,21):
        if testnum%i==0:
            b=b+1
    if b==20:
        return True
   
for i in range(1,300000000):
    if i%100000 == 0:
        print(i)
    if checkdivisibility(i)==True:
        print (i)
print ('done')
