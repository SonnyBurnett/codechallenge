def fibonacci(limit):
    sequence = [1, 2]
    while True:
        next_num = sequence[-1] + sequence[-2]
        if next_num < limit:
            sequence.append(next_num)
        else:
            break

    return sequence


print(sum([x for x in fibonacci(4000000) if x % 2 == 0]))

