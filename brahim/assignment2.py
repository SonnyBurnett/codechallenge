def sum_even_fibonacci(max_term):
    first_term = 1
    second_term = 2
    sum_even_fibo = 0
    while second_term <= max_term:
        if second_term % 2 == 0:
            sum_even_fibo += second_term
            
        temp = first_term
        first_term = second_term
        second_term = temp + second_term
    
    return sum_even_fibo

max_term = 4000000
print(sum_even_fibonacci(max_term))
