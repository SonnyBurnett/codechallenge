# Initialize
x = [0,1]
index = 1

# Loop as logn as fibonacci value is less than 4 million
while x[index] < 4000000:
    x.append((x[index]+x[index-1]))
    index += 1

# Remove the last added value
x.remove(x[index])
print(sum([i for i in x if (i % 2 == 0)]))