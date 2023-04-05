def removeblank(lis):
    while lis.count([])!=0:
       del lis[lis.index([])]
    return lis
def length(lis):
    length=0
    for item in lis:
        length=length+len(item)
    print (length)
def getsquare(num,direc):
    if (num**0.5)%1==0:return num
    if direc=='up':return int((((num**0.5)-((num**0.5)%1))+1)**2)
    if direc=='dn':return int(((num**0.5)-((num**0.5)%1))**2)
def getdirec(num,size,orig):
    squareu=getsquare(num,'up')
    squared=getsquare(num,'dn')
    if (num-size)==squared and (squared**0.5)%2==0:return'rt'
    if ((num-1)**0.5)%1==0 and ((num-1)**0.5)%2==1:return 'dn'
    if ((num-1)**0.5)%2==0 and ((num-1)**0.5)%2==0:return 'up'
    if 1+num-size==squared and (squared**0.5)%2==1:return 'lt'
    return orig
def insert(lis,num,size,direc):
    s=int((size-1)/2)
    mid=int((len(lis)+1)/2)
    if direc=='rt':lis[mid-s].append(num)
    if direc=='lt':lis[mid+s].insert(0,num)
    if direc=='up':lis[int(mid+1+s-(num-(((num**0.5)-(num**0.5)%1)**2)))].insert(0,num)
    if direc=='dn':lis[int(mid-s+(num-(((num**0.5)-(num**0.5)%1)**2)))].append(num)
    return lis
def makespiral(size):
    spiral=[]
    for i in range(size):
        spiral.append([])
    spiral[int((size+1)/2)].append(1)
    spiral[int((size+1)/2)].append(2)
    return spiral
def getulam(sizea):
    spiral=makespiral(sizea*3)
    direc='lt'
    size=3
    for num in range(3,(sizea**sizea)+1):
        if ((num-1)**0.5)%1==0 and ((num-1)**0.5)%2==1:
            size=size+2
            print(size)
        if size>sizea: break
        spiral,direc=insert(spiral,num,size,getdirec(num,size,direc)),getdirec(num,size,direc)
    return removeblank(spiral)
def sumdiagonals(spiral):
    pos=0
    s=0
    for i in spiral:
        s=s+i[pos]+i[len(spiral)-pos-1]
        pos=pos+1
    s=s-1
    return s
print (sumdiagonals(getulam(1001)))


