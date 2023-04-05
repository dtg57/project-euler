
def nextrow(lastrow):
    lastrow = [0] + lastrow
    row = []
    if len(lastrow) % 2 == 0:
        for i in range((len(lastrow)) // 2):
            row.append(lastrow[i] + lastrow[i + 1])
        row = row + row[::-1]
        return row
    else:
        for i in range((len(lastrow) + 1) // 2):
            row.append(lastrow[i] + lastrow[i + 1])
        temp = row[:-1]
        row = row + temp[::-1]
        return row

def pascal(rows):
    triangle = [[1]]
    for i in range(rows - 1):
        triangle.append(nextrow(triangle[-1]))
    return triangle

def checkdiv7(rows):
    triangle = pascal(rows)
    primes = [2, 3, 5, 7]
    divcount = {2:0, 3:0, 5:0, 7:0}
    for a in triangle:
        for b in a:
            for i in primes:
                if b % i == 0:
                    divcount[i] += 1
    return divcount


import math
factorials = {}

def factorial(n):
    global factorials
    if n in factorials:
        return factorials[n]
    else:
        ans = math.factorial(n)
        factorials[n] = ans
        return ans

def pascalcell(a, b):
    if a == 0 or b == 0:
        return 1
    return factorial(a)/(factorial(b) * factorial(a - b))

def divpascal(rows):
    primes = [2, 3, 5, 7]
    divcount = {2:[], 3:[], 5:[], 7:[]}
    for row in range(rows):
        for cell in range(row + 1):
            n = pascalcell(row, cell)
            for i in primes:
                if n % i == 0:
                    divcount[i].append(n)
                    break
    return divcount

def maketriangle(rows):
    triangle = []
    for row in range(rows):
        rownow = []
        for cell in range(row + 1):
            rownow.append(pascalcell(row, cell))
        triangle.append(rownow)
    return triangle

def proportions(divnums, rows):
    total = (rows * (rows + 1)) // 2
    print(total)
    for i in divnums:
        now = divnums[i]
        print(i, now/total)

rows = 10**9
count = checkdiv7(rows)
print(count)
#proportions(divpascal(rows), rows)
proportions(count, rows)


