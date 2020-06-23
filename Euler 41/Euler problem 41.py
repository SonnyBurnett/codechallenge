import math,time

start_time = time.process_time()

def isPrime(number):
    for j in range(3,int(math.sqrt(number))+1,2):
        if number%j == 0:
            return False
    return True

def checkPandigital(number, length):
    return all([str(i) in str(number) for i in range(1, length+1)])
        
def generatePandigital():
    minimum = 1234566
    maximum = 7654321
    for i in range(maximum, minimum,-2):
        if checkPandigital(i,7):
            yield i
    minimum = 1233
    maximum = 4321
    for i in range(maximum, minimum,-2):
        if checkPandigital(i,4):
            yield i

for i in generatePandigital():
    if isPrime(i):
        print(i)
        break

print(time.process_time() - start_time)
