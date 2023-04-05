import math

def choose(n, r):
    return math.factorial(n)/(math.factorial(r) * math.factorial(n - r))

def prob2H(M):
    T = 0.5
    HT = 0.25
    HH = 0.25
    s = 0
    N = M - 2
    if N % 2 == 0:
        top = int(N/2)
    else:
        top = int((N-1)/2)
    for i in range(0, top + 1):
        s += T**(N - 2*i) * HT**i * choose(N - i, i)
    return s * HH

s = 0

for i in range(3, 100, 3):
    s += prob2H(i)
    print(i, ' ', prob2H(i))

