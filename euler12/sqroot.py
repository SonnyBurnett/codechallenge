import math

n = 28
cnt = 0
for i in range(1, (int)(math.sqrt(n)) + 1):
    if (n % i == 0) : 
            print("{ng}/{ig} == {ig}".format(ng=n,ig=i))
            if (n / i == i) : 
                cnt = cnt + 1
                print("Added cnt + 1: " + str(cnt))
            else : 
                cnt = cnt + 2 
                print("Added cnt + 2: " + str(cnt))