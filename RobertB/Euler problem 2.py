result = 0
last_fib_num = 1

next_fib_num = 2



while next_fib_num <= 4000000:
	result += next_fib_num

	for i in range(3):

		temp = next_fib_num
		next_fib_num += last_fib_num
		last_fib_num = temp



print(result)