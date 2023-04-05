import random
p=[1,2,3,4]
c=[1,2,3,4,5,6]
prolls=[]
crolls=[]
def getrolls(start,posses):
    total=0
    for i in posses:
        total+=start[i]
    return total
for pposa in range(4):
    for pposb in range(4):
        for pposc in range(4):
            for pposd in range(4):
                for ppose in range(4):
                    for pposf in range(4):
                        for pposg in range(4):
                            for pposh in range(4):
                                for pposi in range(4):
                                    prolls.append(getrolls(p,[pposa,pposb,pposc,pposd,ppose,pposf,pposg,pposh,pposi]))
for cposa in range(6):
    for cposb in range(6):
        for cposc in range(6):
            for cposd in range(6):
                for cpose in range(6):
                    for cposf in range(6):
                        crolls.append(getrolls(c,[cposa,cposb,cposc,cposd,cpose,cposf]))
pcounts = {}
ccounts = {}
pconstant = 466560000/262144
cconstant = 2621440000/46656

for i in prolls:
    if i not in pcounts:
        pcounts[i] = 1
    else:
        pcounts[i] += 1
for i in crolls:
    if i not in ccounts:
        ccounts[i] = 1#*(262144/46656)
    else:
        ccounts[i] += 1#*(262144/46656)

print(pcounts,ccounts)
pscore = 0
cscore = 0
for i in pcounts:
    pscore += pcounts[i] * i * (46656/262144)n
for i in ccounts:
    cscore += ccounts[i] * i 
total = cscore + pscore
print(pscore/total, cscore/total)
