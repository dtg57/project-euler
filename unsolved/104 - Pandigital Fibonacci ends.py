fibdone = {1:1, 2:1}
t = '123456789'
def fib(n):
    global fibdone
    if n in fibdone:
        return fibdone[n]
    if n - 1 in fibdone and n - 2 in fibdone:
        fibdone[n] = fibdone[n - 1] + fibdone[n - 2]
        return fibdone[n]
    t = [1, 1]
    for i in range(n - 1):
        t = [t[1], t[0] + t[1]]
    ans = t[0]
    fibdone[n] = ans
    fibdone[n + 1] = t[1]
    return ans

def pandig(n):
    if '0' in n:
        return False
    global t
    for i in t:
        if i not in n:
            return False
    return True

def pandigboth(n):
    n = str(n)
    start = n[:9]
    end = n[-9:]
    if pandig(start):
        if pandig(end):
            return True
    return False

ans = 0
n = 53800
while ans == 0:
    if n % 100 == 0:
        print(n)
    f = fib(n)
    if pandigboth(f):
        ans = n
    n += 1
print(ans)


'''
print(pandig('576789231'))
'''
