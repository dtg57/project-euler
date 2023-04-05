def getarea(x, y):
    return 0.5 * x * (y ** 2 - (0.5 * x) ** 2) ** 0.5
print(getarea(6, 5))

s = 0
for side in range(2, 333333334, 1):
    if side * 3 - 1 >= 1000000000:
        continue
    if side % 10000 == 0:
        print(side, s)
    a = getarea(side + 1, side)
    b = getarea(side - 1, side)
    if a % 1 == 0:
        #print(side, side + 1, side)
        s += side * 3 + 1
    if b % 1 == 0:
        #print(side, side - 1, side)
        s += side * 3 - 1
print(s)   
'''
print(getarea(6, 5), getarea(10, 11))
'''
