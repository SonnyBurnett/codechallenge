i = 0
iNext = 1
sum = 0

while iNext <= 4000000:
    if iNext % 2 == 0:
        sum = sum + (iNext)
    iNext = iNext + i
    i = iNext - i

print(sum)
