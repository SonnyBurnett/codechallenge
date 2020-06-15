import math

# count the divisors 
def cntDiv(numDiv) : 
    cnt = 0
    for i in range(1, (int)(math.sqrt(numDiv)) + 1) : 
        if (numDiv % i == 0) : 
            

            if (numDiv / i == i) : 
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



    


   