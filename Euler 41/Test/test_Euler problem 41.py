import math, unittest

def isPrime(number):
    for i in range(3,int(math.sqrt(number))+1,2):
        if number%i == 0:
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

def test_isPrime():
    try:
        assert not isPrime(289) 
        assert not isPrime(111) 
        assert isPrime(37)
    except:
        print("Test isPrime() failed")
    finally:
        print("Test isPrime() completed")

def test_checkPandigital():
    try:
        assert checkPandigital(1234567, 7)
        assert checkPandigital(2461375, 7)
        assert not checkPandigital(1234587, 7)
        assert not checkPandigital(1034567, 7)
        assert not checkPandigital(1234568, 7)
        assert checkPandigital(1234, 4)
        assert checkPandigital(2413, 4)
        assert not checkPandigital(1235, 4)
        assert not checkPandigital(1034, 4)
    except:
        print("Test checkPandigital() failed")
    finally:
        print("Test checkPandigital() completed")

def test_generatePandigital():
    F = generatePandigital()
    try:
        assert next(F) == 7654321
        assert next(F) == 7654231
        assert next(F) == 7654213
        assert next(F) == 7654123
        assert next(F) == 7653421
    except:
        print("Test generatePandigital() failed")
    finally:
        print("Test generatePandigital() completed")

test_isPrime()
test_checkPandigital()
test_generatePandigital()