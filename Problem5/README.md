# Explanation
The question is basically asking for the LCM between numbers from 1 to 20,
for which we need to ensure that we only include the prime factors. However, some prime factors occur more than once. For example the LCM of numbers from 1 to 6 is _2x3x2x5_ (2 occurs twice).

What determines the exponent here for a prime factor, say p, is the greatest power of p that is less than or equal to 20. 
For example: the greatest power of 2 that is less than 20 is 4 since *2^4(=16)* < 20 but *2^5(=32)* > 20. Similarly for 3, it's 2 since _3^3(=27)_ is > 20.
We can further note that the exponent, say e, is 1 for p > sqrt(20) 
i.e. we only need to evaluate e for p <= sqrt(20).

We can thus derive a formula:

Let's say we have an array of primes p[1], p[2]... p[i] and their respective exponents are e[1], e[2]... e[i].

Then we can write,

p[i]^e[i] = 20

Taking log on both sides, we have

e[i]xlog(p[i]) = log(20)

e[i] = log(20) // log(p[i])   [doing floor division (denoted by '//') as e must be an integer]

__Hence for a particular prime 'p',__

___e = log(20) // log(p)___

Multiplying all of the prime numbers with the thus obtained powers (e) raised, we should get the LCM (N).
