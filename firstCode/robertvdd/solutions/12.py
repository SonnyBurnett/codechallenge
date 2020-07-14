from util import list_factors

# python generator, keep infinitly procuding new values on demand
def triangle_gen():
    t, i = 0, 1
    while True:
        t += i
        i += 1
        yield t


for t in triangle_gen():
    if len(list_factors(t)) > 500:
        print(t)
        break
        
'''        
Run 4
   Does it run 0.5. Yes it runs but very slowly
   Names OK: 0.5  Methods names good, loop variable i good. But 't'?
   Linted: 1
   Language: 0.5 Roll your own loops... but they are very clear
   Single Responsibility: 0.5. Would normally have given 1, but there are 'this is what I am doing comments' (not API documentation or 'why' comments) 
   DeepSource: 1
   Tests: 0

 '''
  
  
