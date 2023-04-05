with open('p102_triangles.txt') as file:
    lines = file.readlines()
    
triangles = {}
pos = 0

def midpoint(coords):
    av = [(coords[0][0] + coords[1][0]) / 2, (coords[0][1] + coords[1][1]) / 2]
    x = coords[2][0] + (2/3) * (av[0] - coords[2][0])
    y = coords[2][1] + (2/3) * (av[1] - coords[2][1])
    return [x, y]

for i in lines:
    c = i.strip('\n').split(',')
    line = []
    for i in c:
        line.append(int(i))
    triangles[pos] = [[line[:2], line[2:4], line[4:]]]
    pos += 1

def lineeq(points):
    gradient = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
    intercept = points[0][1] - gradient * points[0][0]
    return [gradient, intercept]

def alllineeqs(coords):
    eqs = []
    eqs.append(lineeq(coords[:2]))
    eqs.append(lineeq([coords[0], coords[2]]))
    eqs.append(lineeq(coords[1:]))
    return eqs

def checkpoint(point, line):
    return ((line[1][0] - line[0][0]) * (line[1][1] - point[1]) - (line[1][1] - line[0][1]) * (line[1][0] - point[0])) > 0

def checkfororigin(triangle):
    lines = [[triangle[0][0], triangle[0][1]], [triangle[0][0], triangle[0][2]], [triangle[0][1], triangle[0][2]]]
    checks = []
    for line in lines:
        checks.append(checkpoint(triangle[1], line))
    originchecks = []
    for line in lines:
        originchecks.append(checkpoint([0, 0], line))
    return checks == originchecks

for i in range(0, 1000):
    if i in [127, 522, 582]:
        continue
    triangles[i].append(midpoint(triangles[i][0]))
    triangles[i].append(alllineeqs(triangles[i][0]))

count = 0
for i in triangles:
    if i in [127, 522, 582]:
        continue
    c = checkfororigin(triangles[i])
    if c:
        count += 1

print(count)

