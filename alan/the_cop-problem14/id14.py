# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.
collatz_dict = {}

def get_collatz_chain(number):
    global collatz_dict
    sequence_chain = [number]
    while number != 1:
        if number in collatz_dict:
            if sequence_chain[0] % 2 != 0:
                collatz_dict[sequence_chain[0]] = len(sequence_chain)+collatz_dict.get(number)-1
            return len(sequence_chain)+collatz_dict.get(number)-1
        if (number % 2) == 0:
            number /= 2
            sequence_chain.append(number)
        else:
            number = 3*number+1
            sequence_chain.append(number)
    for number in range(0,len(sequence_chain)):
        if sequence_chain[number] % 2 != 0:
            collatz_dict[sequence_chain[number]] = len(sequence_chain)-number
    return len(sequence_chain)
if __name__ == "__main__":
    test_chain = get_collatz_chain(26)
    answer_dict = {}
    startnumber = 2
    for number in range(startnumber, 1000000):
        answer_dict[number] = get_collatz_chain(number)
        number += 1
    print(max(answer_dict.keys(), key=(lambda key: answer_dict[key])))
    pass