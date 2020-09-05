"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

import time

start_time = time.time()
palindromes = []

for i in range(100, 1000):
    for j in range(100, 1000):
        k = i * j
        if str(k) == str(k)[::-1]:
            palindromes.append(k)
            
palindromes.sort()

print(f"The largest palindrome made from the product of two 3-digit numbers is {palindromes[-1]}.")
print(f"Program finished in {time.time() - start_time}s.")
