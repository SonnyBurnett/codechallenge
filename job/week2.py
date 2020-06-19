# Euler Problem 2 - Even Fibonacci numbers
x = 0
y = 1
z = 4000000
outcome = 0

fibonacci = [x, y]

# calculate fibonacci numbers
while ((fibonacci [(len (fibonacci)-1)])+(fibonacci [(len (fibonacci)-2)])) < z:
    fibonacci.append (((fibonacci [(len (fibonacci)-1)])+(fibonacci [(len (fibonacci)-2)])))
print (fibonacci)

# calculate sum of even fibonacci numbers
for num in fibonacci:
     if not num%2:
             outcome += num
             
print (outcome)
