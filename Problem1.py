"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time

multiples = []
start_time = time.time()

for i in range(3, 1000):
	if (i % 3 == 0) or (i % 5 == 0):
		multiples.append(i)

print(sum(multiples))

print(f"[Program finished in {round((time.time() - start_time), 5)} seconds]")