def sumdigit(num):
    string=str(num)
    sumd=0
    for dig in string:
        sumd=sumd+int(dig)
    return sumd
def allpowers(limit):
    powers=[]
    for a in range(1,limit):
        for b in range(1,limit):
            powers.append(a**b)
    return powers
powers=allpowers(100)
mx=0
for power in powers:
    if sumdigit(power)>mx:mx=sumdigit(power)
print (mx)
