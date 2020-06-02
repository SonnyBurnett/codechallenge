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


if __name__ == "__main__":
    
    divisor = 0
    tn = 0
    n = 0

    while divisor < 500:
        n += 1
        tn = (int)((n*(n+1))/2)
        #print("tn"+str(tn))
        divisor = cntDiv(tn)

    outstr = "Triangulare number is : {trnum}, Number of divisors: {divnum}".format(trnum = tn,divnum=divisor)

    print(outstr)



    


   