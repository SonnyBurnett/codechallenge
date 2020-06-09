#Euler 2
#Even Fibonacci numbers

def fib_sum_even(n):
    """Set variable of the function"""
    sum = 0
    a = 0
    b = 1
    fiblist = []
    """Loop till 4.000.000"""
    while a < n:
        if a % 2 == 0:
            sum = (sum + (a))
            fiblist.append(a)
        if b % 2 == 0:
            sum = (sum + (b))
            fiblist.append(b)
        a = a + b
        b = b + a
    return sum, fiblist

#Calls the function and prints the returned value
x, y = fib_sum_even(4000000)
print(str(x) + " is the total of " + str(len(y)) + " even Fibonacci numbers: " + str(y).strip('[]'))







