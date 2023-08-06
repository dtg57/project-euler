# Problem 70: Totient Permutation
# Solved: 02/08/23
# Runtime: 03:34

from prime_test_factorise import primeFactorise

# prime factorises n, then counts the number of each prime factor and outputs dictionary of counts
def primeFactorCounts(n):
    prime_factors = primeFactorise(n)
    counts = {}
    for prime_factor in prime_factors:
        if prime_factor in counts:
            counts[prime_factor] += 1
        else:
            counts[prime_factor] = 1
    return counts

# totient function, using the formula phi(n) = n * product(1 - 1/1p) for all unique prime factors p of n
def totient(n):
    prime_factor_counts = primeFactorCounts(n)
    unique_prime_factors = list(prime_factor_counts.keys())
    product = 1
    for prime_factor in unique_prime_factors:
        product *= n - n/prime_factor
    return int(product / n**(len(unique_prime_factors) - 1))

# verifies if integers m and n are permutations of each other
def checkPerm(m,n):
    str_m = str(m)
    str_n = str(n)
    if len(str_m) != len(str_n):
        return False
    for i in range(0,10):
        str_i = str(i)
        if str_m.count(str_i) != str_n.count(str_i):
            return False
    return True

# finds the minimum integer n between 2 and upper (inclusive) such that n / phi(n) is minimised, and phi(n) is a permutation of n
def totientMinimumPerm(upper):
    totient_minimum = False
    n_minimum = False
    for n in range(2,upper+1):
        if n%100000 == 0:
            print(n)
        totient_n = totient(n)
        if checkPerm(n, totient_n):
            test = n / totient(n)
            if (not totient_minimum) or test < totient_minimum:
                n_minimum = n
                totient_minimum = test
    return n_minimum, totient_minimum

print(totientMinimumPerm(10**7))