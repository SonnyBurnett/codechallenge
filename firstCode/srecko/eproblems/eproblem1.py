'''
Score 6.5 
   Does it run 1.5 (bonus point because it's the fastest solution)
   Names OK: 1
   Linted: 1
   Language: 1. Nice to see a main method! Use of //. 
   Single Responsibility: 1 Nice to see 
   DeepSource: 1  <--- Taco please check
   Tests: 0

NOTE: 
Please avoid premature optimisation in your helper. It made the code less clear and Premature Optimisation is the Root Of All Evil.
If it changed the 'order of' or avoided 'N+1' that's different of course. 

Also: Use of 'input' prohits any easy automated tests, and makes it much harder to change/reuse anything we write

API Comments aren't a negative, but they reduce the readability of the code, and make it harder to understand what is happening. 
Using good names for variables makes the code easier to read, and easier to understand. 
'''


def sum_total(n, m):
    """Calculate the sum up to the number given in parameter a in steps of parameter b.

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
