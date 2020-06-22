def sumevenfibonaccinumbers(firstnumber, maxvalue):

    if type(firstnumber) != int:
        raise TypeError("The first parameter should be an integer.")
    if firstnumber < 0:
        raise ValueError("The first parameter should be a non-negative number.")
    if type(maxvalue) not in [int, float]:
        raise TypeError("The second parameter should be an integer or a float.")
    if maxvalue < firstnumber:
        raise ValueError("The second parameter should be higher than the first parameter.")

    fibsequence = fibonaccisequence(firstnumber)

    if firstnumber not in fibsequence:
        raise ValueError("the first parameter is not a valid Fibonacci number.")

    allfibnrsinrange = []
    allfibnrsinrange.extend(fibsequence[-2:])

    sumevenfibnrsinrange = 0
    for number in allfibnrsinrange:
        if number % 2 == 0 and number <= maxvalue:
            sumevenfibnrsinrange += number

    i = sum(allfibnrsinrange[-2:])

    while i <= maxvalue:
        if i % 2 == 0:
            sumevenfibnrsinrange += i

        allfibnrsinrange.extend([i])
        i = sum(allfibnrsinrange[-2:])

    print(sumevenfibnrsinrange)
    return sumevenfibnrsinrange


def fibonaccisequence(maxnumber):
    fibsequence = [0, 1]
    i = sum(fibsequence[-2:])

    while i <= maxnumber:
        fibsequence.extend([i])
        i = sum(fibsequence[-2:])

    fibsequence.extend([i])
    return fibsequence

