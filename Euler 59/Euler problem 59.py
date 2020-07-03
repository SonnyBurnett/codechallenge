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


with open('p059_cipher.txt', 'r') as f:
    largetxt = (f.read()).split(",")

largetxt = [int(i) for i in largetxt]
 
position1=[]
position2=[]
position3=[]

for i in range(int(len(largetxt))):
    if i%3 == 0:
        position1.append(largetxt[i])
    if i%3 == 1:
        position2.append(largetxt[i])
    if i%3 == 2:
        position3.append(largetxt[i])

key1 = xor(most_frequent(position1),32)
key2 = xor(most_frequent(position2),32)
key3 = xor(most_frequent(position3),32)

decrypt1 = [xor(i,key1) for i in position1]
decrypt2 = [xor(i,key2) for i in position2]
decrypt3 = [xor(i,key3) for i in position3]

decrypt = ""

for i in range(len(decrypt1)):
    decrypt += chr(decrypt1[i])
    if i < len(decrypt2):
        decrypt += chr(decrypt2[i])
    if i < len(decrypt3):
        decrypt += chr(decrypt3[i])

print(decrypt)
print(sum(decrypt1)+sum(decrypt2)+sum(decrypt3))
