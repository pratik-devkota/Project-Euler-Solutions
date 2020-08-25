def prime_factors(n):
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
print(f"Upen is a bitch: {time.time() - start_time}s.")