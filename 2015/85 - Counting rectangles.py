import math
def getrects(l, w):
    a = math.factorial(l + 1) / (math.factorial(l - 1) * 2)
    b = math.factorial(w + 1) / (math.factorial(w - 1) * 2)
    return int(a * b)
closest = [10000000, [0, 0, 0]]
for a in range(1, 500):
    print(a)
    for b in range(1, 500):
        rects = getrects(a, b)
        if abs(2000000 - rects) < closest[0]:
            closest = [abs(2000000 - rects), [a, b, rects]]
            #print(closest)
print(closest)
