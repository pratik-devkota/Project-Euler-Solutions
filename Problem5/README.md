<p>
<h2> Explanation </h2>
The question is basically asking for the LCM between numbers from 1 to 20,
for which we need to ensure that we only include the prime factors. However, some prime numbers occur more than once. For example the LCM of numbers from 1 to 6 is <i>2*3*2*5</i> <b>(2 occurs twice)</b>. </br>
What determines the exponent here for a prime number, say <i>p</i>, is the greatest power of <i>p</i> that is less than or equal to 20. 
For example: the greatest power of 2 that is less than or equal to 20 is 4 since <i>2**4(=16) < 20</i> but <i>2**5(=32) > 20</i>.
Similarly for 3 it's 2 since <i>3**3(=27) > 20</i>.
We can further note that the exponent, say <i></i>, is 1 for <i>p > square root of 20</i>. 
i.e. we only need to evaluate e for p <= sqrt(20)
</br>
We can derive a formula for it:
Let's say we have an array of primes p[1], p[2]... p[i] and their respective exponents are e[1], e[2]... e[i]
Then we can write:
p[i] ** e[i] = 20
Taking log on both sides, we have
e[i]log(p[i]) = log(20)
<h6> e[i] = log(20) / log(p[i]) </h6>
<i>(doing floor division as e must be an integer)</i>
</br>
<h6>Hence for a particular prime,
e = log(20) // log(p)</h6>

Multiplying all of the prime numbers with the thus obtained powers <i>(e)</i> raised, we should get the LCM <i>(N)</i>.
</p>