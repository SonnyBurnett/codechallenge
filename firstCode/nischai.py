import timeit
def myFunc():
    total = 0
    for i in range(1,1000):
        if ((i % 3 == 0) or (i % 5 == 0)):
            total += i
            print(i)
    print ("Total = " + str(total))

print(timeit.timeit(myFunc, number=1))
"""
 Score:
    Run 1 Not sure if it works. Would need to check
    NamesOK 0.5.  myfunc??. But total is a nice name, and i is good
    Linted1
    Libraries list / 0.5  Used language features. The function isn't parameterised so no points in single responsibility, and really it has no value to the project.
    SingleResponsibility/0
    Deepsource/1
    Testing 0/3
    
Score 4/10
"""
