# Problem #3

## Task

Project Euler 41: We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

## Reduce of calculations

We have 1..n (where n = 9). In order to reduce amount of calculations we want to check the following: 

9+8+7+6+5+4+3+2+1 = 45, 45/3 = 15
8+7+6+5+4+3+2+1 = 36, 36/3 = 12
7+6+5+4+3+2+1 = 28, 28/3 = 9.3
6+5+4+3+2+1 = 21, 21/3 = 7
5+4+3+2+1 = 15, 15/3 = 5
4+3+2+1 = 10, 4/3 = 1.3
3+2+1 = 6, 6/3 = 2
2+1 = 3 3/3 = 1

The above is based on division by 3 rule (if the sum of all digits in number divisible by 3, then the whole number is divisible by 3). With that we can say that only pandigital numbers with 7 and 4. Since we need largest, we want to evalute everything below 7654321. 

So the solution would be to:

1. Check if the number is prime
2. And is pandigital

The largest would be the answer.

## Result

7652413