import math
third = (1/3)
hcftried = {}

def hcf(no1, no2):
    global hcftried
    num1 = no1
    num2 = no2
    tuples = [(no1, no2), (no2, no1)]
    if tuples[0] in hcftried:
        return hcftried[tuples[0]]
    if tuples[1] in hcftried:
        return hcftried[tuples[1]]
    while no1 != no2:  
        if no1 > no2:  
            no1 -= no2  
        elif no2 > no1:  
            no2 -= no1
    #addmany(num1, num2, no1)
    return no1

def addmany(num1, num2, gcd):
    global hcftried
    a = num1
    b = num2
    while a < 12005:
        hcftried[(a, num2)] = gcd
        a += a
    a = num1
    while b < 12005:
        hcftried[(num1, b)] = gcd
        b += a
    return hcftried

def getrange(dem):
    bottom = math.floor(dem/3)
    if bottom == 0:
        bottom += 1
    return bottom, math.ceil(dem/2)+1

def isdiv(divisors, num):
    for i in divisors:
        if num % i == 0:
            return True
    return False

def relativeprimes(num):
    divisors = {}
    rprimes = []
    r = getrange(num)
    for i in range(r[0], r[1]):
        if not isdiv(divisors, i):
            if hcf(num, i) == 1:
                rprimes.append(i)
            else:
                divisors[i] = 0
    return rprimes

def getreducedfracs(dem):
    global third
    count = 0
    nums = relativeprimes(dem)
    for num in nums:
        frac = num/dem
        if frac < 0.5 and frac > third:
            count += 1
    return count
        
total = 980764
for i in range(2,12001):
    if i % 100 == 0:
        print(i, total)
    total += getreducedfracs(i)
print (total)

