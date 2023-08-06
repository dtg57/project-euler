# Problem 69 - Totient Maximum
# Solved: 02/08/23
# Runtime: 00:16

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
        product *= 1 - 1/prime_factor
    return int(n * product)

# finds the max value of n which produces teh maximum n / phi(n) between 1 and upper bound specified (inclusive)
def totientMaximum(upper):
    totient_maximum = 0
    n_maximum = 0
    for n in range(2, upper+1):
        totient_n = totient(n)
        if totient_n <= 0:
            print('zero totient: ', n, totient_n)
        test = n/totient(n)
        if test > totient_maximum:
            totient_maximum = test
            n_maximum = n
    return n_maximum

print(totientMaximum(10**6))