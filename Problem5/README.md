# Explanation
The question is basically asking for the LCM between numbers from 1 to 20,
for which we need to ensure that we only include the prime factors. However, some prime factors occur more than once. For example the LCM of numbers from 1 to 6 is 2*3*2*5 (2 occurs twice).
What determines the exponent here for a prime factor, say p, is the greatest power of p that is less than or equal to 20. 
For example: the greatest power of 2 that is less than 20 is 4 since 2^4(=16) < 20 but 2^5(=32) > 20.
Similarly for 3 it's 2 since 3^3(=27) > 20.
We can further note that the exponent, say e, is 1 for p > sqrt(20). 
i.e. we only need to evaluate e for p <= sqrt(20)

We can thus derive a formula:
Let's say we have an array of primes p[1], p[2]... p[i] and their respective exponents are e[1], e[2]... e[i]
Then we can write,
p[i]^e[i] = 20
Taking log on both sides, we have
e[i]*log(p[i]) = log(20)
Doing floor division (denoted by '//') as e must be an integer,
e[i] = log(20) // log(p[i])

Hence for a particular prime,
#### e = log(20) // log(p)

Multiplying all of the prime numbers with the thus obtained powers (e) raised, we should get the LCM (N).
