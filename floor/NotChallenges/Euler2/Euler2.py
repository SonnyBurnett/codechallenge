def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def determine_sum_even_valued_fib_num():
    fib_num_list = [1, 1]
    sum_even_fib_num = 0

    four_million = False
    while not four_million:
        fib_num_list.append(sum(fib_num_list))
        del fib_num_list[0]

        if is_even(fib_num_list[1]):
            sum_even_fib_num += fib_num_list[1]

        if fib_num_list[1] >= 4000000:
            four_million = True

    return sum_even_fib_num


def fib():
    a, b = 1, 2
    while 1:
        yield a
        a, b = b, a+b


if __name__ == "__main__":
    sum = determine_sum_even_valued_fib_num()
    print(sum)