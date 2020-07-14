def get_sum_of_multiples(max_number):
    number_list = [*range(0, max_number, 1)]

    return sum(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, number_list)))

if __name__ == "__main__":
    sum = get_sum_of_multiples(1000)
    print(f'Here is the sum of multiples: {sum}')
    
"""    
Score:
    Run 1 Not sure if it works. Would need to check
    NamesOK 1.  i is a loop variable not a list. 
    Linted 1
    Libraries list / 1  really nice
    SingleResponsibility/0.5 It's nice to see the function. It would have been really nice to see the lambda injected, but even so this is nice
    Deepsource/1
    Testing 0/3
    
Score 5.5/10
"""
