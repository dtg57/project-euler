def getsides(p):
    solutions=[]
    for a in range(1,p):
        for b in range(1,p-a):
            c=p-a-b
            if a<c and b<c and a<b:
                if a**2+b**2==c**2:
                    solutions.append([a,b,c])
    return solutions
sols=[]
mx,high=0,0
for i in range(1,1001):
    print (i)
    sols.append([i,getsides(i)])

for i in sols:
    if len(i[1])>mx:
        mx=len(i[1])
        high=i
print (high)
