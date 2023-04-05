with open('p079_keylog.txt') as file:
    content=[x.strip ('\n') for x in file.readlines()]
attempts={}
for i in content:
    attempts[i]=0

def join(a,b):
    a,b=str(a),str(b)
    diffs={}
    for i in range(1,min(len(a),len(b))-1):
        if a[i:]==b[:len(b)-i]:
            diffs[(a+b[i:])]=0
        if a[:len(a)-i]==b[i:]:
            diffs[b+a[i:]]=0
    return diffs
def findvalid(maybes):
    def check1(i):
        i=list(i)
        for b in digs:
            if b not in i:
                return False
        return True    
    posses=[]
    digs=['0','1','2','3','6','7','8','9']
    for i in maybes:
        if check1(i):
            posses.append(i)
    return posses
def getmaybes(start):
    maybes={}
    for a in start:
        for b in start:
            if a==b:
                continue
            else:
                maybes.update(join(a,b))
    return maybes
maybes=attempts
#while len(findvalid(maybes))>0:
#    maybes=getmaybes(maybes)
#    print(maybes)
#for i in findvalid(maybes):
#    print(i)
print(getmaybes(maybes))


    
