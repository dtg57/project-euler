def getnext(num):
    s=0
    for i in list(str(num)):
        s+=int(i)**2
    return s
to89={}
to1={}
count=0
for i in range(1,10000000):
    if i%1000==0:
        print(i,count)
    if i in to89:
        count+=1
        continue
    if i in to1:
        continue
    chain=[i]
    while True:
        nex=getnext(chain[-1])
        chain.append(nex)
        if nex==1 or nex==89:
            break
    if chain[-1]==89:
        for b in chain:
            to89[b]=0
        count+=1
        continue
    if chain[-1]==1:
        for b in chain:
            to1[b]=0
        continue
print(count)       
