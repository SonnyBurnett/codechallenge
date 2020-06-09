def sum_even_fibo(maxvalue):
    prevone = 1
    prevtwo = 0
    i = 0
    checkeven = 0
    sumeven = 0
    #limit the fibonacci value
    while (prevone + prevtwo) <= int(maxvalue):
        i = prevone + prevtwo
        checkeven = i/2
        #only add even values
        if i % 2 == 0:
            sumeven = sumeven + i     
        #move to next value
        prevtwo = prevone
        prevone = i
    return (sumeven)
 
 #call the function
 sum_even_fibo(4000000)
