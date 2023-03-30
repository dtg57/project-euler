import math

# ordered list of primes that is updated as and when new primes are needed for isPrime() and primeFactorise()
primes = [2, 3, 5]

# dictionary with structure  {number : array of prime factors, ...}
prime_factors_dict = {}
        
# 
# results if given number n is prime
# Returns tuple, first element is bool (True if prime); second element is a factor if not prime, 0 if prime
# Works by checking if n is divisible by all primes up to sqrt(n)
#
def isPrime(n):
    global primes
    if n == 1:
        return (False, 0)
    if n in primes:
        return (True, 0)
    sqrt = math.ceil(math.sqrt(n))
    for div in primes:
        if div > sqrt:
            return (True, 0)
        if n%div == 0:
            return (False, div)
    div_cand = div
    new_prime_count = 0
    while div_cand < sqrt or new_prime_count == 0:
        if div_cand %2 == 0:
            div_cand += 1
        else:
            div_cand += 2
        # recursively check whether div_cand is prime as we only need to result whether n is divisible by primes
        if isPrime(div_cand)[0]:
            new_prime_count += 1
            primes.append(div_cand)
            if n%div_cand == 0:
                return (False, div_cand)
    return (True, 0)

#
# Finds the prime factors of n
# Returns array of prime factors (not ordered). If there are repeated factors, these appear multiple times, e.g. 12 gives [2, 2, 3]
#
def primeFactorise(n):
    global prime_factors_dict
    if n in prime_factors_dict:
        return prime_factors_dict[n]
    prime_factors = []
    if n == 1:
        return [1]
    is_prime = isPrime(n)
    if is_prime[0]:
        return [n]
    # result stores the current result after dividing n by all the prime factors found so far. We search for prime factors of this and divide until result itself is prime
    result = n
    while not is_prime[0]:
        prime_factors.append(is_prime[1])
        result = int(result/is_prime[1])
        # use our stored prime factors of other numbers to speed this up
        if result in prime_factors_dict:
            return prime_factors + prime_factors_dict[result]
        is_prime = isPrime(result)
    prime_factors.append(result)
    prime_factors_dict[n] = prime_factors
    return prime_factors  
