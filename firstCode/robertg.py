"""
Score: 3.5
    Run 0.5 OK it works but it spams the monitor with junk, and is horribly slow
    NamesOK 0. i is good. x/y/z???
    Linted 1
    Libraries list 1
    SingleResponsibility/0
    Deepsource/1
    Testing 0/3
    
Score 4.5/10
"""



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
