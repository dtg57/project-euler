import time
def getfib(pos):
    track = (0, 1)
    for i in range(pos - 1):
        track = (track[1], track[1] + track[0])
    return track[0]
def nimsum(p1, p2, p3):
    end = (p1^p2)^p3 != 0
    return (p1^p2)^p3 != 0
def getnims(power):
    count = 0
    for i in range(1,2**power+1):
        if not nimsum(i, 2*i, 3*i):
            count += 1
    return count
print (getfib(33))
