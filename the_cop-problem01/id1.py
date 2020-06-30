# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
import sys
sys.setrecursionlimit(1500)

output = 0 
def check(i):
    global output
    if (i % 5) == 0 or (i % 3) == 0:
        output = output + i
    if i != 1:
        check(i-1)

if __name__ == "__main__":
    check(999)
    print(output)