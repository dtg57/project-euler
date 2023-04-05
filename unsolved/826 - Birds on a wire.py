# Problem 826: Birds on a wire
# Solved: in progress
# Runtime:
#
# I thought I'd derived the correct formula for F(n) = (3n-1)/(4n+4), so below I was adding this up over all primes < 10^6 and averaging.
# I got this by finding the average distance between two consecutive points when n points are picked randomly along a line of length 1.
# This distance is 1/(n+1). Then I considered the intervals between adjacent points.
# If the interval increases (i.e. distance from 1st to 2nd point is smaller than distance from 2nd to 3rd) then we label it binary 1; if decreases then label it 0.
# Concatenate all these binary digits for a given set of points. E.g. for 5 points we will have a 3 digit binary number, say 101, representing an arrangement like | x  x     x x     x |
# The number of '10' in this binary number gives the number of non-painted intervals on this wire. Therefore, we count the number of '10's in all binary numbers with n-2 digits (there is a recursive formula for this)
# Find the average fraction of unpainted intervals for n birds, subtract from 1, and multiply by the average interval size 1/(n+1). This gives the above F(n).
#
#
# Turns out this is the wrong answer, so below I was running some random samples and getting an idea for what F(n) should be.
# It seems F(n) decreases with n, asymptoting to ~0.39 as n gets large. So my formula is not correct.
# This is likely because not all binary numbers (labelling the intervals, see above) have equal probability - need to investigate further.
#

import prime_test_factorise
import random

probs = []
for i in range(3,10**4,2):
    if prime_test_factorise.isPrime(i)[0]:
        probs.append((3*i-1)/(4*i+4))

print(len(probs))
print(round(sum(probs)/len(probs),10))

# run some random samples
n = 1000
it = 10000
painteds = []
for i in range(it):
    birds = sorted([random.uniform(0,1) for j in range(n)])
    #print(birds)
    intervals_painted = []
    nearest_neighbours = {}
    for j in range(n):
        if j == 0:
            nearest_neighbours[j] = 1
        elif j == n-1:
            nearest_neighbours[j] = n-2
        else:
            nearest_neighbours[j] = j+1 if birds[j+1] - birds[j] < birds[j] - birds[j-1] else j-1
    #print(nearest_neighbours)
    for bird in nearest_neighbours:
        intervals_painted.append(tuple(sorted((bird, nearest_neighbours[bird]))))
    #print(intervals_painted)
    intervals_painted = set(intervals_painted)
    length_painted = 0
    for interval in intervals_painted:
        length_painted += birds[interval[1]] - birds[interval[0]]
    #print(intervals_painted, length_painted)
    painteds.append(length_painted)
    #print(length_painted)
print(sum(painteds)/it)