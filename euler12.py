import math

# count the divisors 
def cntDiv(n) : 
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if (n % i == 0) : 
            
            if (n / i == i) : 
                cnt = cnt + 1
            else : 
                cnt = cnt + 2
                  
    return cnt 


divisor = 0
tn = 0
n = 0

while divisor < 500:
    n += 1
    tn = (n*(n+1))/2
    divisor = cntDiv(tn)
    
print("Triangulare number is : " + str(tn))



    


   