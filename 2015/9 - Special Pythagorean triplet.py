import math
nums=[]
for i in range(1,1001):
    nums.append(i)

triplets=[]
posa=0
posb=0
posc=0

for i in range(999):
    for i in range(999):
        for i in range(999):
            if nums[posa]+nums[posb]+nums[posc]==1000 and nums[posa]**2+nums[posb]**2==nums[posc]**2 and nums[posa]<nums[posb]:
                triplets.append([nums[posa],nums[posb],nums[posc]])
            posa=posa+1
        posa=0
        posb=posb+1
    posb=0
    print (posc)
    posc=posc+1

print (triplets)
