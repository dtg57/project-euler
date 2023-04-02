# Problem 146: Investigating a Prime Pattern
# Solved: in progress
# Runtime:
#
# Currently my method is brute-force with some shortcuts. It is taking way too long, minutes for 10^6 so will be hours for 1.5*10^8. There must be other shortcuts.


import prime_test_factorise
import time

def time_statement(eval_statement):
    time_start = time.perf_counter_ns()
    eval(eval_statement)
    time_end = time.perf_counter_ns()
    return time_end - time_start


valid_n = []
primes_test_true = [1,3,7,9,13,27]
# For the given numbers to be consecutive primes, n^2+11, n^2+17, n^2+21 and n^2+23 must not be prime.
primes_test_false = [11,17,21,23]
max = 10**6

# If n is not a multiple of 10, then one of n^2+1, n^2+3, n^2+7, n^2+9 will be a multiple of 5. Therefore only test multiples of 10.
for n in range(10, max, 10):
    # If n is a multiple of 3, say n=3x then n^2 + 3 = 3(3x^2 + 1), so not prime. Same for 7 and 13.
    if n%3 == 0 or n%7 == 0 or n%13 == 0:
        continue
    if n%10000 == 0:
        print(n)
    n_squared = n**2
    for i in primes_test_true:
        #print(n,i)
        if not prime_test_factorise.isPrime(n_squared + i)[0]:
            break
    else:
        for i in primes_test_false:
            #print(n,i)
            # if n is a multiple of 11 then n^2+11 is not prime, so skip the primality test
            if n%i == 0:
                continue
            if prime_test_factorise.isPrime(n_squared + i)[0]:
                break
        else:
            valid_n.append(n)

print(prime_test_factorise.primes)
print(time_statement('prime_test_factorise.isPrime(12111)'))
print(time_statement('110%11'))

print(valid_n)