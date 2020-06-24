import argparse
from collections import defaultdict, Counter

# Global variables: Have the poker rules in both human readable text and in comparable "magic".
str_order = '0123456789TJQKA'
ranked_names = ['NONE', 'High Card', 'One Pair', 'Two Pairs', 'Three of a Kind', 'Straight', 'Flush', 'Full House',
                'Four of a Kind', 'Straight Flush', 'Royal Flush']
ranked_order = [0, (1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (1, 1, 1, 1, 1), (1, 1, 1, 1, 1), (3, 2),
                (4, 1), (1, 1, 1, 1, 1), (1, 1, 1, 1, 1)]
ranked_list = list(enumerate(ranked_names))
subranked_name = ['High Card', 'Straight', 'Flush', 'Straight Flush', 'Royal Flush']
subranked_order = [(5, 2), (5, 2), (5, 1), (5, 1), (5, 1)]
subranked_list = list(zip([1, 5, 6, 9, 10], subranked_name))


def get_list_id(name):
    """This method translates a human readable score into a comparable value from the ranked list.

    :param name: Name
    :type name: str
    :return int: game ranked value
    """
    helper = [item for item in ranked_list if item[1] == name]
    return helper[0][0]


def is_subranked(list_in):
    """Method returns True is the input list is matching fine 1 in a row.

    :param list_in: list set of five int values
    :type list_in: [int]
    :return bool: True or False
    """
    return list_in == (1, 1, 1, 1, 1)


def get_sublist_id(name):
    """This method translates a human readable score into a comparable value from the sub-ranked list.
    This method is an anti pattern (Copy and past programming) of the get_list_id method,
        but this is to make the same look and feel in the control program.
    Note that the sub-ranked list has been build on purpose in the same way as the ranked list (using list and zip).

    :param name: name of the human readable rank in the ranked names list
    :type name: str
    :return int: game ranked value
    """
    helper = [item for item in subranked_list if item[1] == name]
    return helper[0][0]


def sequence(list_in):
    """This method uses the sorted input list and self created list from the minimum and maximum vale of the input list
    this enables you to simply compare them.

    :param list_in: a sorted or unsorted list of integers.
    :type list_in: list of int
    :return bool: True if the list contains sequential numbers.
    """
    return sorted(list_in) == list(range(min(list_in), max(list_in) + 1))


def ranked_as(rawhandvalue, rawsuitvalue):
    """This method handles the control logic for calculating the ranked hand values including their highest cards in
    order and also returns the leftover cards to identify the highest cards in case of draws.

    :param rawhandvalue: a default dict of the card values of a hand
    :param rawsuitvalue: a default dict of the suit values of a hand
    :return: a list with a list ranked value with the order of highest card(s)
                and the leftover cards ordered from high to low to break ties.
    """
    ranked_state_id = get_list_id('NONE')
    ranked_tie_breaker = []
    tie_breaker = []

    sorted_hand_value = sorted(rawhandvalue, key=None, reverse=True)
    list_num, list_occ = zip(*Counter(rawhandvalue).most_common(5))

    if is_subranked(list_occ):
        if len(rawsuitvalue) > 1:
            if sequence(sorted_hand_value):
                ranked_state_id = get_sublist_id('Straight')
                ranked_tie_breaker.append(sorted_hand_value[0])
            else:
                ranked_state_id = get_sublist_id('High Card')
                ranked_tie_breaker.append(sorted_hand_value[0])

        elif (len(rawhandvalue), len(rawsuitvalue)) == (5, 1):
            if sequence(sorted_hand_value):
                if sorted_hand_value[0] == 14:
                    ranked_state_id = get_sublist_id('Royal Flush')
                    ranked_tie_breaker.append(sorted_hand_value[0])
                else:
                    ranked_state_id = get_sublist_id('Straight Flush')
                    ranked_tie_breaker.append(sorted_hand_value[0])

            else:
                ranked_state_id = get_sublist_id('Flush')
                ranked_tie_breaker.append(sorted_hand_value[0])

    else:
        ranked_state_id = get_list_id(ranked_names[ranked_order.index(list_occ)])
        ranked_tie_breaker.append(list_num[0])
        if ranked_state_id == get_list_id('Full House'):
            ranked_tie_breaker.append(list_num[1])

    for i in range(len(list_num)):
        if list_occ[i] == 1:
            tie_breaker.append(list_num[i])

    return (ranked_state_id, ranked_tie_breaker), sorted(tie_breaker, key=None, reverse=True)


def eproblem54(file_in):
    """Starting method to read the file and initialize the complex type dicts,
        pass it to the ranked control and compare the two hands from the lines in the data.

    :param file_in: the file name where the data is to be compared
    :type: str
    :return: the wins of player one
    """
    f = open(file_in, "r")
    wins_p1 = 0
    wins_p2 = 0

    for line in f:
        hand1value = defaultdict(int)
        hand1suit = defaultdict(int)
        hand2value = defaultdict(int)
        hand2suit = defaultdict(int)

        hands = line.split()
        for card in range(0, 5):
            hand1value[str_order.index(hands[card][0])] += 1
            hand1suit[hands[card][1]] += 1

        for card in range(5, 10):
            hand2value[str_order.index(hands[card][0])] += 1
            hand2suit[hands[card][1]] += 1

        if ranked_as(hand1value, hand1suit) > ranked_as(hand2value, hand2suit):
            wins_p1 += 1
        else:
            wins_p2 += 1

    f.close()

    print("Player 1 wins ", wins_p1, " hands.")
    return wins_p1


def main():
    """"Main is the interactive method start of the second project Euler problem,
        reasoning is documented in the '../notebooks/Project Euler Problem 54.ipynb' notebook.
        This method has anti pattern (Input kludge) and cannot be tested without a human or screen scraper,
         but used for the interactive guided demonstration of the Notebooks.

    """
    file_name = input("File Name to read: ")
    eproblem54(file_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", help="Set input file")
    args = parser.parse_args()

    if not isinstance(args.file, type(None)):
        eproblem54(args.file)
    else:
        main()
