import math
import time
divisors = {}
def getdivs(num):
    global divisors
    if num in divisors:
        return divisors[num]
    count = 1
    for i in range(1,math.ceil(num/2)+1):
        if num % i == 0:
            count += 1
    divisors[num] = count
    return count
def getsmallest(divs):
    test = 2
    while getdivs(test) < divs:
        test += 1
    return test
for i in range(2,100):
    print(i, getsmallest(i))
    #time.sleep(1/2)
