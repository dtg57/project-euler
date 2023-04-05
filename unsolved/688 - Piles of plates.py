import math

M = 1000000007

def modsum(arr):
    global M
    s = 0
    for i in arr:
        s+= i%M
    return s%M

def tri(n):
    return int(0.5 * n * (n + 1))

def arctri(n):
    return (math.sqrt(1 + 8*n) - 1) / 2

def sumForFixedK(k, n):
    if n < tri(k):
        return 0
    if (k%1 !=0):
        raise NameError('Rubbish')
    mid = (n - tri(k) + 1)
    b = math.floor(mid / k)
    ans = k * tri(b) + (b + 1) * (mid - b * k)
    #print(mid, ' ', b, ' ', k, ' ', ans)
    if (ans%1!=0):
        raise NameError('Rubbish')
    return ans

def sumOfAll(N):
    a=[]
    global M
    for i in range(1, math.ceil(math.sqrt(2*N)+1000000)):
        if (i % 100000 == 0):
            print (i)
        a.append(sumForFixedK(i, N))
    return a


s = sumOfAll(10**16)
print(len(s))
print(sum(s))
print(modsum(s))
print(sum(s)%M)

    
    
