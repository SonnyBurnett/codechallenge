three = 0
five = 0
for x in range(1000):
	if(x % 3 == 0):
	    three = three + x
	elif(x % 5 == 0):
	    five = five + x
print("The sum of all the multiples of 3 or 5 below 1000 = ", three + five)
