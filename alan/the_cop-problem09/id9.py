# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

def find_pythagorean_triplet(max_int):
    for x in range(1,max_int-2):
        for y in range(x,max_int-x):
            z = max_int-x-y
            if x < y < z:
                if math.sqrt(((x**2)+(y**2))) == z:
                    print("Found {} + {} + {} = {}".format(x,y,z, (x+y+z)))
                    print("Euler solution: {}".format(x*y*z))
if __name__ == "__main__":
    find_pythagorean_triplet(1000)