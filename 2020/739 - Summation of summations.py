# Problem 739: Summation of summations
# Solved: 27/12/2020
# Runtime: 6:54

import math
from time import perf_counter as stamp

mod = 1000000007
n = 10**8

def fermat_compute(n,p):
    facts = [0]*n
    invfacts = [0]*n

    facts[0] = 1
    invfacts[0] = 1
    for i in range(1,n):
        if (i%10**6) == 0: print(i)
        # calculate factorial and corresponding inverse
        facts[i] = (facts[i-1]*i)%p
        invfacts[i] = pow(facts[i],p-2,p)

    return facts, invfacts

facts, invfacts = fermat_compute(2*n, mod)

def chooseMod(n, r):
    global facts, invfacts, mod
    return (facts[n] * ((invfacts[r]*invfacts[n-r] % mod))) % mod
    '''global mod
    if r > n:
        return 0
    if r ==0 or r==n:
        return 1
    if r ==1 or r == n-1:
        return n % mod
    num = 1
    for i in range(n, n-r, -1):
        num = (num*i) % mod
    denom = 1
    for i in range(1, r+1):
        denom = (denom*i) % mod
    return (num*pow(denom, mod - 2, mod)) % mod'''

#Extended Euclidian Algorithm for the modular inverse, i.e. to find the number x such that ax = 1 mod b
def modularInverse(a, b):
    x,y, u = 0,1, 1
    while a != 0:
        q, r = b//a, b%a
        m = x-u*q
        b,a, x, u = a,r, u, m
    gcd = b
    return x

def J(m, n):
    global mod
    times = {'ChooseMod' : 0,
              'Mod1' : 0,
              'Pow' : 0,
              'Mod2' : 0,
              }
        
    t1 = stamp()
    choose = chooseMod(2*m - n, m - n)
    t2 = stamp()
    times['ChooseMod'] = t2 - t1
    Mod1 = ((n+1) * choose) % mod
    t1 = stamp()
    times['Mod1'] = t1 - t2
    Pow = pow(m+1, mod - 2, mod)
    t2 = stamp()
    times['Pow'] = t2 - t1
    Mod2 = (Pow * Mod1) % mod
    t1 = stamp()
    times['Mod2'] = t1 - t2
    
    return [Mod2, times]

root5 = math.sqrt(5)
phi = (1+root5)/2
invphi = -1/phi

def Lucas(i):
    global phi, invphi, root5
    return (phi**(i-1) - invphi**(i-1) + 3*phi**i - 3*invphi**i) / root5

def f(n):
    totaltimes = {'ChooseMod' : 0,
              'Mod1' : 0,
              'Pow' : 0,
              'Mod2' : 0,
              }
    s = 0
    Lucas = (1,3)
    for i in range(0,n - 1):
        if i%10000 == 0:print(i)
        j = J(n - 2, i)
        s += j[0] * Lucas[1]
        for a in j[1]:
            totaltimes[a] += j[1][a]
        s %= mod
        Lucas = (Lucas[1] % mod, (Lucas[0] + Lucas[1]) % mod)
    return s, totaltimes

print(f(n))

