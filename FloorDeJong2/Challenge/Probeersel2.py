from collections import Counter

card_value = Counter([3, 4, 5, 5, 6])
print(card_value)
print(card_value.values())
if (3 in card_value.values()) & (2 in card_value.values()):
    print("Yes, 3 eand 2")

if all(x in card_value.values() for x in [3, 2]):
    print("Yes, 3 eand 2")

if Counter(card_value.values())[1] == 5:
    print("Yes")

print(sorted(card_value.keys()))
print(list(range(min(card_value.keys()), max(card_value.keys()) + 1)))
if sorted(card_value.keys()) == list(range(min(card_value.keys()), max(card_value.keys()) + 1)):
    print(True)