def sum_fibo(n_max, n_add):
    """Calculate the Fibonacci number given in parameter n_max and then adds additional steps as given by n_add.

    :param n_max: fist number indicates the Fibonacci number that may not be exceeded.
    :param n_add: second number indicates the additional Fibonacci steps that can be added after reaching the max.
    :return: fn the result of the sum Fibonacci sequence with overflow.
    """
    fn, f1, f2 = 0, 1, 1

    while fn <= n_max:
        fn = f2 + f1
        f1, f2 = f2, fn

    for i in range(1, n_add, 1):
        fn = f2 + f1
        f1, f2 = f2, fn

    return fn


def main():
    """"Main method of the second project Euler problem,
        reasoning is documented in the '../notebooks/Project Euler Problem 2.ipynb' notebook.

    """
    target: int = int(input("Search for even Fibonacci sum below: "))

    print("Total sum of even Fibonacci numbers: ", int((sum_fibo(target, 2) - 1) * 0.5))


if __name__ == "__main__":
    main()
