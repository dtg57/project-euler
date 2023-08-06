# Problem 60: Prime Pair Sets
# Solved: 02/08/23
# Runtime: 9:07

import math
from prime_test_factorise import isPrime
import time

start = time.time()

# Generate all primes between m and n inclusive
def genPrimes(m, n):
    primes = []
    for i in range (m, n+1):
        if isPrime(i)[0]:
            primes.append(i)
    return primes

# concatenates two integers without resorting to str()
def concatIntegers(m, n):
    digits_n = math.ceil(math.log10(n))
    return m * 10**digits_n + n

def recursiveSetFind(n_target, n, primes, current_sets, sum_threshold):
    print(n)
    if n == 0:
        new_sets = [[prime] for prime in primes]
        return recursiveSetFind(n_target, 1, primes, new_sets, sum_threshold)
    elif n < n_target:
        new_sets = []
        for current_set in current_sets:
            sum_current = sum(current_set)
            current_max = max(current_set)
            for new_prime in primes:
                # do not examine sets with too large a sum
                # only add primes higher than the current max prime
                if new_prime > current_max and sum_current + new_prime < sum_threshold:
                    concat_works = True
                    for current_prime in current_set:
                        # check all concat pairs are prime
                        if not (isPrime(concatIntegers(current_prime, new_prime))[0] and isPrime(concatIntegers(new_prime, current_prime))[0]):
                            concat_works = False
                            break
                    if concat_works:
                        new_sets.append(current_set + [new_prime])
                        if n == n_target - 1:
                            print(new_sets[-1])
        return recursiveSetFind(n_target, n+1, primes, new_sets, sum_threshold)
    else:
        return current_sets



n = 5
# test primes above this lower limit and below this threshold
prime_lower = 3
sum_threshold = 5*10**4
prime_threshold = 1 *10**4

primes = genPrimes(prime_lower, prime_threshold)
sets = recursiveSetFind(n, 0, primes, [], sum_threshold)

min_set = []
min_sum = False
for s in sets:
    if sum(s) < min_sum or not min_sum:
        min_set = s
        min_sum = sum(s)

print(min_set, min_sum)

end = time.time()

print(end - start)