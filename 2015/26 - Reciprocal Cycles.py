import pdb
def stringify(lis):
    ans=''
    for i in lis:ans=ans+i
    return ans
def getdec(no,div):
    num=list(str(no))
    for i in range(1000):
        num.append('0')
    ans=''
    if div>no:
        ans='0.'
    pos,it=0,1
    for i in range(900):
        b=0
        c=0
        while div<int(num[c]):
            pos,b=pos+1,b+1
            ans=ans+'0'
            c=c+1
        if it==1:
            p=stringify(num[pos-b:pos+1])
        ans=ans+str(int(p)-(int(p)%div))
        p=int(str(int(stringify(num[pos-b:pos+1]))%div)+num[pos+1])
        it,pos=it+1,pos+b
    return ans
print (getdec(1,2))


