def sum_total(n, m):
    """Calculate the sum up to the number given in parameter n in steps of parameter m.

    :param n: fist number indicates the total sum that needs to be calculated
    :param m: second number is the step size of the sum(s)
    :return: result of the sum up to the total multiplied by the step
    """
    helper = n // m  # Trick to reuse divides are costly operations

    if n % m == 0:
        result = m * helper * (helper - 1) * 0.5
    else:
        result = m * helper * (helper + 1) * 0.5

    return result


def main():
    """"Main method of the first project Euler problem,
        reasoning is documented in the '../notebooks/Project Euler Problem 1.ipynb' notebook.

    """
    target: int = int(input("Search for multiples below: "))
    first_div: int = int(input("Lower prime divider: "))
    second_div: int = int(input("Higher prime divider: "))

    common_div = first_div * second_div

    print("Total sum of prime multiples: ",
          int(sum_total(target, first_div) + sum_total(target, second_div) - sum_total(target, common_div))
          )


if __name__ == "__main__":
    main()
