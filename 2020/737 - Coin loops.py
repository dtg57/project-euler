# Problem 737: Coin loops
# Solved: 13/12/2020
# Runtime: 15:36

import cmath
import math

theta = 0
turns = 0
n = 1
com = 1
reset = 1
thetaprev=0

while turns < 2022:
    n += 1
    thetaprev=theta
    theta = cmath.phase(com) + math.acos(abs(com)/2)
    if theta > math.pi:
        theta -= 2 * math.pi
        reset = 0
    if reset==0 and theta>0:
        turns += 1
        print (turns, ' ', n, ' ', theta/(math.pi)*180, ' ', (theta - thetaprev)/math.pi*180)
        reset = 1
    com = ((n-1) * com + cmath.exp(1j*theta)) / (n)
