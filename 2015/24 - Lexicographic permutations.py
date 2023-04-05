import itertools
p=itertools.permutations(['1','2','3','4','5','6','7','8','9','0','a'])
perms=[]
for i in p:
    perms.append(''.join(i))
print(sorted(perms)[999999])
