""" Question:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import math
import time

start_time = time.time()

def prime_numbers(k):
    """ Gives a list of prime numbers from 2 to k """
    p = []
    for i in range(2,k+1):
        for j in range(2,i):
            if((i % j) == 0):
                break
        else:
            p.append(i)
    return p

k = 20
# N will be the LCM
N = 1
i = 0

primes = prime_numbers(k)
limit = math.sqrt(k)
check = True

while True:
    if i >= len(primes):
        break
    e = 1
    if check:
        if e <= limit:
            e = math.log(k) // math.log(primes[i])
        else:
            check = False
            
    N = N * (primes[i]**e)
    i = i + 1

print(f"The smallest number divisible by all of the numbers from 1 to {k} is {N}.")
print(f"[Program finished in {round(time.time() - start_time, 5)} seconds]")
