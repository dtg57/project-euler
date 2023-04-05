def checkspecial(num):
    n=list(str(num))
    if n[-1]!='0':
        return False
    pos=0
    for i in range(1,10):
        if n[pos]!=str(i):
            return False
        pos+=2
    return True
def increase3(num):
    num=list(str(num))
    num[1]=str(int(num[1])+1)
    num[2]='2'
    num=int(''.join(num))
    return num
square=int(1020000000000000000**0.5)
while True:
    if str(square**2)[2]!='2':
        square=int((increase3(square**2))**0.5)
    if square%10000==0:print(square**2)
    if checkspecial(square**2):
        print(square)
        break
    square+=1
    
    
