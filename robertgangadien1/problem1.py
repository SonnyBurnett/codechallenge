z = 0
for i in range(1, 1000):
    x = i/3
    y = i/5
    if ".0" in str(x) and i >=3:
        print (i, x)
        z = z + i
    elif ".0" in str(y) and i >= 5:    
        print (i, y)
        z = z + i       
 
print(z)
