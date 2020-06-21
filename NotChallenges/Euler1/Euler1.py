def get_sum_numbers_dividable_by(dividor_one, dividor_two, range_num):
    sum = 0
    for number in range(range_num):
        if (number % dividor_one == 0) or (number % dividor_two == 0):
            sum += number
    return sum


if __name__ == '__main__':
    sum = get_sum_numbers_dividable_by(3, 5, 1000)
    print(sum)
