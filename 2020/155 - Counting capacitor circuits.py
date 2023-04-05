# Problem 155: Counting Capacitor Circuits
# Solved: 23/12/2020
# Runtime: 06:11
#
# We solve this problem recursively.
# Start with one capacitor C, there is only circuit that can be made, so only possible capacitance is C
# Now have two capacitors. Take all the possible one-capacitor circuits (of which there is one) and connect them a) in parallel giving C/2 and b) in series giving 2C
# The only way of adding two integers to get 3 is 1+2=3, so for three-capacitor circuits we combine all 1-capacitor and 2-capacitor circuits a) in parallel and b) in series. Since there are 2 two-capacitor circuits, this gives 2*2=4 values for n=3
# Continue to n = 18, storing all unique capacitances (removing duplicates) at each n
#

import math
from fractions import Fraction

C = 60

# Removes duplicates from array, returning the number of duplicates and the new array
def removeDuplicates(arr):
    new = set(arr)
    return [len(arr) - len(new), new]

# Generates array of all the possible capacitance values for n capacitors, adds this array to dictionary allvals; returns number of new values
def genCombs(n):
    global C
    global allvals
    global toiterate
    if n - 1 not in allvals:
        raise NameError('Calculate vals for ' + str(n-1))
    new = []
    for pair in toiterate[n]:
        for chunk1 in allvals[pair[0]]:
            for chunk2 in allvals[pair[1]]:
                # use Fraction so we avoid floating-point errors (important when removing duplicates)
                series = Fraction(chunk1 * chunk2, chunk1 + chunk2)
                parallel = Fraction(chunk1 + chunk2, 1)
                new += [series, parallel]
    count = len(new)
    # remove duplicates
    [duplicates, cleaned] = removeDuplicates(new)
    print(str(count) + ' values for n = ' + str(n) + ', ' + str(duplicates) + ' of which are duplicates, giving ' + str(count - duplicates) + ' new')
    allvals[n] = cleaned

allvals = {
    1: [C]
}

# for each key n, the value is an array of arrays giving the possible pairs of integers that sum to give n.
# this is used to generate larger circuits from smaller ones already generated, e.g. circuits with 5 capacitors result from combining 1-capacitor and 4-capacitor circuits, and from combining 2-capacitor and 3-capacitor circuits
# we don't need to consider sums of 3 or more integers, e.g. 5 = 1 + 2 + 2, as 3 = 1 + 2 so we will have generated the relevant capacitances with n=3 already
toiterate = {
    2: [[1,1]],
    3: [[1,2]],
    4: [[1,3],[2,2]],
    5: [[1,4],[2,3]],   
    6: [[3,3],[2,4],[1,5]],
    7: [[1,6],[2,5],[3,4]],
    8: [[1,7],[2,6],[3,5],[4,4]],
    9: [[1,8],[2,7],[3,6],[4,5]],
    10: [[1,9],[2,8],[3,7],[4,6],[5,5]],
    11: [[1,10],[2,9],[3,8],[4,7],[5,6]],
    12: [[1,11],[2,10],[3,9],[4,8],[5,7],[6,6]],
    13: [[1,12],[2,11],[3,10],[4,9],[5,8],[6,7]],
    14: [[1,13],[2,12],[3,11],[4,10],[5,9],[6,8],[7,7]],
    15: [[1,14],[2,13],[3,12],[4,11],[5,10],[6,9],[7,8]],
    16: [[1,15],[2,14],[3,13],[4,12],[5,11],[6,10],[7,9],[8,8]],
    17: [[1,16],[2,15],[3,14],[4,13],[5,12],[6,11],[7,10],[8,9]],
    18: [[1,17],[2,16],[3,15],[4,14],[5,13],[6,12],[7,11],[8,10],[9,9]],
}

# populate the allvals dict
for i in range(2,19):
    genCombs(i)

# combine all the values from n = 1,2,...,18 into one array, remove duplicates, and output the total
allvalsarray = []
for n in allvals:
    allvalsarray += allvals[n]
print(len(removeDuplicates(allvalsarray)[1]))

