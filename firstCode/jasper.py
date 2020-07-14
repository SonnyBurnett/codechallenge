'''
Score 3.5
    Run1
    NamesOK 0.5. Please don't damage your code with high maintenance comments that add nothing. Comments should not explain how the code works: the code should be clear enough. A comment is a code smell
    Linted1
    Libraries list / 0 please don't use while true/break. Use the list comprehensions
    SingleResponsibility/0
    Deepsource/1
    Testing 0/3
'''

# start with an int = 1 and use a loop to add 1 in every iteration
# add the integers to a total =>  use a list where every int gets appended to list with every iteration of the loop 
# count % for every integer on the total == 0 => use hte list we have to % every element on the last appended integer and count whenever == 0
# stop when count gtets over 5000
num = 2
i = list(range(1,num))
while True:
    count = 0

    for x in i:
        if num % x == 0:
            count += 1

    if count > 500:
        print(str(num) + ' count: ' + str(count))
        break

    num += 1
    i = list(range(1,num))
