import math
nums=[]
seq='0.'
for i in range(1,1000005):
    nums.append(i)
    if i%10000==0: print(i)
for num in nums:
    if num%10000==0:print(num)
    seq=seq+str(num)
print(int(seq[2])*int(seq[11])*int(seq[101])*int(seq[1001])*int(seq[10001])*int(seq[100001])*int(seq[1000001]))
