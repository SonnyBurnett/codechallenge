'''
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
n = 500

# oneliner
print([((x,y,z), x*y*z, x+y+z) for x in range(n + 1) for y in range(n + 1) for z in range(n + 1) if x<y and y<z and x**2 + y**2 == z**2 and x != 0 and y != 0 and z != 0 and x+y+z==1000])

# results in
# [((200, 375, 425), 31875000, 1000)]
