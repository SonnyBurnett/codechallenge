def get_even_fib(max):
    a, b = 1, 1
    while a <= max:
        if not a%2==0:
            yield a
        a, b = b, a+b
print(sum(get_even_fib(4000000)))
