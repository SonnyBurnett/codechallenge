#list = [1,2,3,4,5,6,7,8,9];
#print(list)
x = 0
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        x += i
print(x)
