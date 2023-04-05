sumsdone = {0:1, 1:1, 2:2, 3:3, 4:5}
pents = [5, 7]
n = 3
def pent(n):
    return int((n * (3 * n) - n) / 2)

while pents[-1] < 1000000:
    pents.append(pent(n))
    pents.append(pent(-n))
    n += 1
#print(pents[:10])
def getpents(below):
    global pents
    a = []
    for i in pents:
        if i <= below:
            a.append(i)
    return a

def getsums(n):
    #p = getpents(n)
    global pents
    global sumsdone
    if n in sumsdone:
        return sumsdone[n]
    s = sums(n - 1) + sums(n - 2)
    it = 0
    sign = False
    for i in pents:
        if i > n:
            break
        if sign:
            s += sums(n - i)
        else:
            s -= sums(n - i)
        it += 1
        if it == 2:
            sign = not sign
            it = 0
    sumsdone[n] = s
    return s
    
def sums(n):
    if n < 0:
        return 0
    global sumsdone
    if n in sumsdone:
        return sumsdone[n]
    else:
        a = getsums(n)
        sumsdone[n] = a
        return a

ans = 0
n = 5
while ans == 0:
    s = sums(n)
    if n % 1000 == 0:
        print(n, len(str(s)))
    if s % (10 ** 6) == 0:
        ans = (n, s)
    n += 1
print(ans)

