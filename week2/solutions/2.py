from util import fibonacci


def sumEvenFibonacci(limit):
    total = 0
    gen = fibonacci()
    while (i := next(gen)) < limit:
        if i % 2 == 0:
            total += i
    return total


def main():
    print(sumEvenFibonacci(4000000))


if __name__ == '__main__':
    main()
