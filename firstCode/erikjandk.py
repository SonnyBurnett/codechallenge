'''
Score 3
   Does it run 0.5 not optimal solution, but OK
   Names OK: 0.5
   Linted: 0.5   Lost half a mark because had lots of comments to explain things: if you need comments... rewrite the code
   Language: 0.5 Used while/break (bad) but also used for loops. List Comprehensions would be much better
   Single Responsibility: 0. It's all one big block of code.
   DeepSource: 1  <--- Taco please check
   Tests:0
   
Please note that the use of comments is a clear indicator of the need for better variable names, and the need to restructure the code
   
   '''

# Init array with prime factors with the first prime 2
pf = [2]
pfi = 1

triNum = 0

# go through all triangular numbers
for i in range(1, 20000):
    triNum += i

	# Init the count of the primes
    pfc = []
    c   = False
    
    j = triNum
    k = 0
    while j > 1:
		# Can it be divided by a prime
        if (j % pf[k]) == 0 :
            if not c:
                pfc.append(0)
                c = True
				
			# Count the prime as a divisor
            pfc[len(pfc)-1] += 1            

            j = int(j/pf[k])
        else:
            c = False
            k +=1

			# if it is a new prime, add it to the list
            if (k >= pfi):
                pfi += 1            
                pf.append(j)

    # calculate divisors for the triangular number = (a+1)(b=1)(c+1).......
    divisors = 1
    for m in range (0,len(pfc)):
        divisors *= (pfc[m]+1)
	
	# if its above 500 print the values and stop the processing
    if divisors > 500:
        print("First Triangular number with more then 500 divisors is " + str(triNum) + " divisors " + str(divisors))
        break
