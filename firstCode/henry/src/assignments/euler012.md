In total I have made three solutions for the given problem.

### Solution 1
The first solution **count_divisors_naive** in functions/count_divsors.py is a naive implementation that finds a solution 
for the given problem. I have not waited a single time for it to run to completion on the given values.

### Solution 2
I assumed that, as with all of these kinds of problems, a more optimal solution for computational time should be exist.
I started hurting my brains for some time on prime factors, a well-known technique for writing larger numbers
as a series of multiplications. However, this assignment did not ask for the prime-factors, but for all possible 
divisors, hence I left this train of thought for a while.

I then came up with the following observation. There is a symmetry in the series of divisors for any number, for any
divisor x there is another divisor x' that follows from value_to_divide / x. Taking this symmetry into account, I
wrote the second function **count_divisors_reduced_by_pairs** in functions/count_divisors.py that implements this approach.
I start enumerating both from 1 up and from the target value down and increment the number of divisors by two, whenever
one is found. I also drop the upper search boundary to x' whenever x is found.

Finally, and this is why we write unit tests, I identified the case of an odd number of divisors using my unit test
for the case of a hundred. Hence I added one more if-clause to correct for the case that x == x' == sqrt(value)

This solution takes 14 - 15 seconds on my machine.

### Solution 3
I could not let of the idea of prime factorization as an even better solution for this problem. Using pen and paper I
made a prime factorization for 1080 (2 * 2 * 2 * 3 * 3 * 3 * 5) and after some puzzeling I saw the math: The divisors 
for 1080 follow from all possible combinations of these prime factors. These combinations can be made by selecting how 
many of each group primes to include (0..number of times a prime is a factor), multiplying those again delivers the 
correct  answer. In this concrete instance 222|333|5 gives 4 * 4 * 2 = 32 divisors for 1080. From here onwards the 
generalization is fairly straight forward and can be found in **count_divisors_reduced_by_primes** in 
functions/count_divisors.py.

I choose a straightforward implementation for generating primes. There are faster implementations, but I ~~had~~ 
wanted to barbecue. 

This solution takes 1,5 seconds on my machine.