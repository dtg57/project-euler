import math
from fractions import Fraction

n = 500

lineSegments = []

s = 629527
m = 500
M = 50515093
lines = []


for i in range(n):
    line = []
    for j in range(2):
        point = ()
        for k in range(2):
            t = s % m
            point += (t,)
            s = s**2 % M
        line.append(point)
    lines.append(line)

def checkIntersect(line1, line2):
    if (line1[1][1] - line1[0][1] == 0):
        if (line2[1][1] - line2[0][1] == 0):
            return False
        grad2 = Fraction(line2[1][0] - line2[0][0], line2[1][1] - line2[0][1])
        y0 = line1[1][1]
        if (line2[0][1] < y0 and y0 < line2[1][1]) or (line2[0][1] > y0 and y0 > line2[1][1]):
            x0 = (y0 - line2[1][1]) * grad2 + line2[1][0]
            return (x0, y0)
        return False
        
    if (line2[1][1] - line2[0][1] == 0):
        grad1 = Fraction(line1[1][0] - line1[0][0], line1[1][1] - line1[0][1])
        y0 = line2[1][1]
        if (line1[0][1] < y0 and y0 < line1[1][1]) or (line1[0][1] > y0 and y0 > line1[1][1]):
            x0 = (y0 - line1[1][1]) * grad1 + line1[1][0]
            return (x0, y0)
        return False
        
    grad1 = Fraction(line1[1][0] - line1[0][0], line1[1][1] - line1[0][1])
    grad2 = Fraction(line2[1][0] - line2[0][0], line2[1][1] - line2[0][1])
    if grad1 == grad2:
        return False
    y0 = Fraction(line2[1][0] - line1[1][0] + grad1 * line1[1][1] - grad2 * line2[1][1], grad1 - grad2)
    #print(grad1, ' ', grad2, ' ', y0)
    if ((line1[0][1] < y0 and y0 < line1[1][1]) or (line1[0][1] > y0 and y0 > line1[1][1])) and ((line2[0][1] < y0 and y0 < line2[1][1]) or (line2[0][1] > y0 and y0 > line2[1][1])):
        x0 = Fraction(grad1 * grad2 * (line2[1][1] - line1[1][1]) + line1[1][0] * grad2 - line2[1][0] * grad1, grad2 - grad1)
        return (x0, y0)
    return False

intersects = []

for i in range (n):
    line1 = lines[i]
    if i %1 == 0:
        print(i, ' ', len(intersects))
    for j in range(i+1, n):
        line2 = lines[j]
        a = checkIntersect(line1, line2)
        if a:
            #print(a, ' ', i, ' ', j)
            intersects.append(a)



print('length = ' + str(len(set(intersects))))
        

        
        
