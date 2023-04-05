sumsdone = {0:1, 1:1, 2:2, 3:3, 4:5}
pents = [5, 7, 12, 15, 22, 26, 35, 40, 51, 57, 70, 77, 92, 100]

def getsums(n):
    global pents
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

print(getsums(100))

    
