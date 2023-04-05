import math

def maxinlist(lis):
    mx=0
    for i in range(len(lis)):
        if lis[i]>mx:
            mx=i
    return mx

def nextterm(num):
    if num%2==0:
        return num/2
    if num%2==1:
        return (3*num)+1

def collatz(num):
    seq=[num]
    while seq[-1]!=1:
        seq.append(nextterm(seq[-1]))
    return seq

lengths=[]
mx=0

for i in range(1,100000):
    if len(collatz(i))>mx:
        mx=len(collatz(i))
        print (mx,i)
    lengths.append(len(collatz(i)))

print ('Done')

