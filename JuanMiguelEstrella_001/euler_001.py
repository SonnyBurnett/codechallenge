number_limit = 1000
multiple_1 = 3
multiple_2 = 5

print(sum([num for num in range(1, number_limit) if (num % multiple_1 == 0 or num % multiple_2 == 0)]))