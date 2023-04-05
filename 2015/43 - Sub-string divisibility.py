import itertools
perms=itertools.permutations(['1','2','3','4','5','6','7','8','9','0'])
def checkspecial(num):
    def gettriplet(num,pos):
        num=str(num)
        return int(num[pos]+num[pos+1]+num[pos+2])
    divs=[2,3,5,7,11,13,17]
    for i in range(7):
        if gettriplet(num,i+1)%divs[i]!=0:
            return False
    return True
s=0
it=0
for i in perms:
    if it%10000==0:
        print(it)
    if i[0]=='0':
        continue
    num=int(''.join(i))
    if checkspecial(num):
        print('special',num)
        s+=num
    it+=1
print(s)
