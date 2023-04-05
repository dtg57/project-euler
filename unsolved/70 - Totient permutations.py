def hcf(no1,no2):  
    while no1!=no2:  
        if no1>no2:  
            no1-=no2  
        elif no2>no1:  
            no2-=no1  
    return no1
def isdiv(divisors,num):
    for i in divisors:
        if num%i==0:
            return True
    return False
def totient(num):
    count=0
    divisors={}
    for i in range(1,num+1):
        if isdiv(divisors,i):
            continue
        h=hcf(num,i)
        if h==1:
            count+=1
        else:
            divisors[h]=1
    return count
def checkpandig(num1,num2):
    for i in range(10):
        b=str(i)
        if str(num1).count(b)!=str(num2).count(b):
            return False
    return True
minimum=[100,0]
for i in range(87000,10**7,2):
    t=totient(i)
    if checkpandig(i,t):
        print(i)
        rat=i/t
        if rat<minimum[0]:
            print('new min:', i)
            minimum=[rat,i]
            
print(minimum)
    
