'''
Run 3.5 points
   Does it run 0.5 yes but very slowly
   Names OK: 0.5 We can read them and know what they mean, but 'cntDiv'?
   Linted: 0.5 spurious white space
   Language: 1 Nice to see the for loop
   Single Responsibility: 0 Minimal separation 
   DeepSource: 1
   Tests: 0
l'''

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



    


   
