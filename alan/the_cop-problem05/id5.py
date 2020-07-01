# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def solve_problem(i, n):
    for number in range(1,n+1):
        if (i % number) == 0:
            if number != n:
                next
            else:
                return True
        else:
            break
    return False

if __name__ == "__main__":
    if solve_problem(2520,10):
        print("2510 is evenly divisable by all numbers from 1-10")
    if not solve_problem(2521,10):
        print("2511 is not evenly divisable by all numbers from 1-10")
    
    search_break = False
    count_increase = 10000
    x = 1
    y = count_increase    
    while not search_break:
        for test_number in range(x, y):
            if solve_problem(test_number,20):
                print("Smallest number is {}".format(test_number))
                search_break= True
                break
        else:
            x = y
            y = y + count_increase

    