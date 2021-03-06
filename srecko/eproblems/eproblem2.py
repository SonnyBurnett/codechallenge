import argparse


def sum_fibo_div3(n_max):
    """Calculate the Fibonacci number given in parameter n_max and then adds additional steps to be in line with
        dividable by 3.

    :param n_max: fist number indicates the Fibonacci number that may not be exceeded.
    :type n_max: int
    :return: fn the result of the sum Fibonacci sequence with overflow.
    """
    fn, f1, f2 = 0, 1, 1
    count_n = 2

    while fn <= n_max:
        fn = f1 + f2
        f2, f1 = f1, fn
        count_n += 1

    helper = count_n % 3
    if helper == 0:  # Overshot so use the previous fibo
        return f2
    elif helper == 1:  # Need to go to the next n
        return f1 + f2

    return fn


def eproblem2(target):
    """This kick off the calculation for the second project Euler and prints the end result on the screen.
    This method can be initiated from the command line with arguments and used in unit tests.

    :param target: this parameter sets the upper bound of the calculation.
    :return:
    """
    calculate = int((sum_fibo_div3(int(target)) - 1) * 0.5)
    print("Total sum of even Fibonacci numbers: ", calculate)

    return calculate


def main():
    """Main is the interactive start method of the second project Euler problem,
        reasoning is documented in the '../notebooks/Project Euler Problem 2.ipynb' notebook.
        This method has anti pattern (Input kludge) and cannot be tested without a human or screen scraper,
         but used for the interactive guided demonstration of the Notebooks.

    """
    target: int = int(input("Search for even Fibonacci sum below: "))

    eproblem2(target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--below", "-b", help="Search for even Fibonacci sum below value")
    args = parser.parse_args()

    if not isinstance(args.below, type(None)):
        eproblem2(args.below)
    else:
        main()
