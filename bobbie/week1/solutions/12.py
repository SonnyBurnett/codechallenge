from util import list_factors


def triangle_gen():
    """
    triangle generator, keeps infinitly procuding new values on demand
    """
    t, i = 0, 1
    while True:
        t += i
        i += 1
        yield t


def main():
    for t in triangle_gen():
        if len(list_factors(t)) > 500:
            print(t)
            break


if __name__ == '__main__':
    main()
