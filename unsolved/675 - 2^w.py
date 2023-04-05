from Prime_Factoriser import primeFactorise
import math
from itertools import combinations

pascal = {0:{0:1}}
nprimes = 4 #664579

for i in range(1, nprimes + 2):
    pascal[i] = {0:1, 1:i}
    prod = i
    for j in range(2, int(i/2 + 1) if i%2 == 0 else int((i + 1)/2)):
        prod *= i - j + 1
        prod /= j
        pascal[i][j] = int(prod)

def choose(n, r):
    if n in pascal:
        if r in pascal[n]:
            return pascal[n][r]
        elif n - r in pascal[n]:
            return pascal[n][n - r]
    raise NameError('Not enough Pascal calculated')

def addToCounts(pfactor):
    global currenttotalcounts
    global totalpfactors
    if pfactor in totalpfactors:
        totalpfactors[pfactor] += 1
    else:
        totalpfactors[pfactor] = 1
    length = len(totalpfactors)
    for i in range(0, length):
        combs = choose(length + 1, i)
        if i+1 in currenttotalcounts:
            currenttotalcounts[i+1] += combs
        else:
            currenttotalcounts[i+1] = combs

def addToOverall():
    global overallcounts
    global currenttotalcounts
    for n in currenttotalcounts:
        if n in overallcounts:
            overallcounts[n] += currenttotalcounts[n]
        else:
            overallcounts[n] = currenttotalcounts[n]
    return

overallcounts = {}
currenttotalcounts = {}
totalpfactors = {}
n = 10

for i in range(2, n + 1):
    if (i%100000==0):print(i)
    pfactors = primeFactorise(i)
    for pfactor in pfactors:
        addToCounts(pfactor)
    addToOverall()
    print(i, ' ', currenttotalcounts)

