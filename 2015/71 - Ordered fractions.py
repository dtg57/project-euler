fracs=[]
import math
for dem in range(2,1000001):
    r=(3/7)*dem
    if dem%10000==0:
        print(dem)
    for num in range(math.floor(r),math.ceil(r)+1):
        fracs.append([(num,dem),num/dem])
closest=[1,0]
for i in fracs:
    t=3/7-i[1]
    if t>0 and t<closest[0]:
        closest=[t,i]
print(closest)
