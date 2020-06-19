def fibnums(num1,num2, lim):
    fib3 = num1 + num2
    total = 0
    if num2%2 == 0:
            total =+ num2
    if fib3 < lim:
        total +=fibnums(num2,fib3, lim)
            
    return total

fiblist = fibnums(1,2,4_000_000)

print(fiblist)
