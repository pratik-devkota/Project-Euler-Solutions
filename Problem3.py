"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

def prime_factors(n):
    """ Gives the largest prime factor for the given number. """
    i = 2
    factors = []
    while i**2 <= n:
        while n > 1:
            while n % i == 0:
                factors.append(i)
                n = n / i
            i += 1
    return factors[-1]
import time
start_time = time.time()

print(prime_factors(600851475143))
print(f"[Program finished in {time.time() - start_time}s.]")
