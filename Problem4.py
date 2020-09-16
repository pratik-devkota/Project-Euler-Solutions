"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

import time

start_time = time.time()

largest_palindrome = 0
a = 999
while a >= 100:
    # three digit numbers are 100-999 (inclusive)
    b = 999
    while b >= a:
        if a*b <= largest_palindrome:
            break # since the product is going to be too small anyway
        if str(a*b) == str(a*b)[::-1]:
            # some Python magic here for reversing the number
            largest_palindrome = a*b
        b -= 1
    a -= 1

print(largest_palindrome)
print(f"Program finished in {time.time() - start_time}s.")
