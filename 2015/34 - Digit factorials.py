import math
def factorialdigits(num):
    lis=list(str(num))
    final=0
    for digit in lis:
        final=final+math.factorial(int(digit))
    if final==num: return True

mx=0
for i in range(3,1000000):
    if factorialdigits(i)==True: mx=mx+i
    if i%10000==0: print (i)
print (mx)
