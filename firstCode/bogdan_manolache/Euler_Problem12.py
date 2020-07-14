'''
Run 3 and 1 bonus
   Does it run 0.5 yes, but very slow
   Names OK: 0.5 
   Linted: 1
   Language: 0 roll your own loops with breaks
   Single Responsibility: 0  
   DeepSource: 1
   Tests: 0
    
Bonus point:
   1 easy to maintain                               
'''                             
from datetime import datetime
import math
start = datetime.now()
n = 1
count = 0

while len(str(n)) <= 500:
 t_number = n*(n+1)/2
 for y in range(1,int(math.sqrt(t_number)) + 1):
  if t_number % y == 0:
      count += 2
  if math.sqrt(t_number) == y:
      count -= 1
 if count >=500:
    break
 count = 0 
 n += 1
print ("Triangular number is= ", t_number)
print("Number of divisors is =", count)
print(datetime.now() - start)
