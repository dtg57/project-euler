# Problem 826: Birds on a wire
# Solved: in progress
# Runtime:
#
# I thought I'd derived the correct formula for F(n) = (3n-1)/(4n+4), so below I was adding this up over all primes < 10^6 and averaging.
# Turns out this is the wrong answer, so below I was running some random samples and getting an idea for what F(n) should be.
# It seems F(n) decreases with n, asymptoting to ~0.39 as n gets large. So my formula is not correct.
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