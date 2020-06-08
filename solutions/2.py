from util import fibonacci

sum = 0
gen = fibonacci()
while (i := next(gen)) < 4000000:
    if i % 2 == 0:
        sum += i 

print(sum)