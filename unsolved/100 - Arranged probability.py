import math
test = 1000031630000
ans = 0
squares = {}
def square(n):
    global squares
    if n in squares:
        return squares[n]
    else:
        s = n ** 2
        squares[n] = s
        return s
def getblues(total):
    global done
    n = total * 0.5 * (total - 1)
    sqrt = math.floor(math.sqrt(n))
    for i in range(sqrt, sqrt + 2):
        if i ** 2 - i == n:
            return i
    return False
while ans == 0:
    if test % 10000 == 0:
        print(test)
    n = getblues(test)
    if n:
        ans = n
    test += 1
print(ans)

