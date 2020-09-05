"""Question:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

import time
start_time = time.time()

def prime_factors(n):
    """ Gives the largest prime factor for the given number. """
    i = 2
    primes = []
    while i**2 <= n:
        while n > 1:
            while n % i == 0:
                primes.append(i)
                n = n / i
            i += 1
    primes.sort()
    return primes[-1]

n = 600851475143

print(f"The largest prime factor of the number {n} is {prime_factors(n)}.")
print(f"[Program finished in {round(time.time() - start_time, 5)}s.]")
