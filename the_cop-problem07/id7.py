# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def get_prim():
    break_listing = False
    return_list = []
    x=2
    while not break_listing:
        for y in range(2,x):
            if (x%y) == 0:
                break
        else:
            return_list.append(x)
            print("{} added to list. List length {}".format(x, len(return_list)))
        if len(return_list) == 10001:
            break_listing = True
        x += 1
    return return_list[-1]

if __name__ == "__main__":
    print(get_prim())
    