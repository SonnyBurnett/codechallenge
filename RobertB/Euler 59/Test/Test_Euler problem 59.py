def asc2bin(asc):
    result = ""
    for j in range(7,0,-1):
        result += str(asc//(2**j))
        asc = asc%(2**j)
    result += str(asc//1)
    return result

def xor(key1asc,key2asc):
    key1bin = asc2bin(key1asc)
    key2bin = asc2bin(key2asc)
    binstring =""

    for k in range(8):
        if key1bin[k]==key2bin[k]:
            binstring += "0"
        else:
            binstring += "1"
    result = 0
    for k in range(8):
        result += (2**(7-k))*int(binstring[k])
    return int(result)

def most_frequent(List):
    countList = [List.count(n) for n in List]
    maxcount = max(countList)
    return List[countList.index(maxcount)]

def test_asc2bin():
    try:
        assert (asc2bin(1) == "00000001")
        assert (asc2bin(11) == "00001011")
        assert (asc2bin(127) == "01111111")
    except:
        print("Test asc2bin() failed")
    finally:
        print("Test asc2bin() completed")
        
def test_xor():
    try:
        assert (xor(65,42) == 107)
        assert (xor(107,42) == 65)
        assert (xor(32,32) == 0)
        assert (xor(85,170) == 255)
    except:
        print("Test xor() failed")
    finally:
        print("Test xor() completed")

def test_mostfrequent():
    try:
        assert (most_frequent([2]) == 2)
        assert (most_frequent([1,2,2]) == 2)
        assert (most_frequent([1,2,1]) == 1)
        assert (most_frequent([1,2,3,2,4,2,5]) == 2)
    except:
        print("Test most_frequent() failed")
    finally:
        print("Test most_frequent() completed")

test_asc2bin()
test_xor()
test_mostfrequent()
