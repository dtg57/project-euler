def getpentag(num):
    return (num*(3*num-1))/2
pentags=[]
for i in range(1,5001):
    pentags.append(getpentag(i))
pos=0
mini=100000000
for a in pentags:
    for b in pentags:
        if b%1000==0: print(a,b)
        if pentags.count(a+b)==1 and pentags.count(abs(a-b))==1 and abs(a-b)<mini:
            mini=abs(a-b)
print (mini)
