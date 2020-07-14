x = 3
y = 999
nums = [x,y]
u = ((((y//x+x//x)/len(nums))*x)*(y//x))

a = 5
b = y
numbers = [a,b]
v= ((((b//a+a//a)/len(numbers))*a)*(b//a))

c = x*a
d = y
numbers = [c,d]
w= ((((d//c+c//c)/len(numbers))*c)*(d//c))

print (u+v-w)

"""
Score 4.5/10
   Does it run: 1.5  Increased this because we didn't want to go back and edit other people's. 
   Names: 0  
   Consistant: 1
   Language features: 0 (because the common code should have been extracted into a function)
   Single Responsibility: 0
   Deep source: 1
   Tests: 0
    
BUT: Cool code, really post
  Bonus point for actually doing the maths, rather than brute force
"""  
    
