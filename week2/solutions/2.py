from util import fibonacci


def main(limit):
    sum = 0
    gen = fibonacci()
    while (i := next(gen)) < limit:
        if i % 2 == 0:
            sum += i
    return sum


if __name__ == '__main__':
    print(main(4000000))
