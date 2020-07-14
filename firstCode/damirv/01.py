#https://projecteuler.net/problem=1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#using list comprehension to iterate up to 1000
#and check for numbers that match criteria mentioned above
print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))


Run 5.5 and 2 bonus points
   Does it run 1
   Names OK: 1
   Linted: 1
   Language: 1
   Single Responsibility: 0 (but we gave a bonus point because it's so cool)
   DeepSource: 1
   Tests: 0.5 ... the code has no tests, but there is nothing go wrong because of good use of language features

Bonus point: 2
  README: 1                  
  It's extremely clear and beautiful
