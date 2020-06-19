from solutions import util


def sumEvenFibonacci(limit):
    total = 0
    gen = util.fibonacci()
    while (i := next(gen)) < limit:
        if i % 2 == 0:
            total += i
    return total


def main():
    print(sumEvenFibonacci(4000000))
