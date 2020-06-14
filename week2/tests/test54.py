import sys
from importlib import import_module

sys.path.append("../solutions")
testSubject = import_module('54')


print("TEST RANKS")
rank = testSubject.Hand(['AD', 'KD', 'QD', 'JD', 'TD']).rank
assert 9 == rank, "got %s, expected 9" % rank
rank = testSubject.Hand(['AD', 'AC', 'AH', 'AS', 'KD']).rank
assert 8 == rank, "got %s, expected 8" % rank
rank = testSubject.Hand(['AD', 'AC', 'AH', 'KD', 'KC']).rank
assert 7 == rank, "got %s, expected 7" % rank
rank = testSubject.Hand(['AD', 'KD', 'QD', 'JD', '2D']).rank
assert 6 == rank, "got %s, expected 6" % rank
rank = testSubject.Hand(['2C', '3C', '4C', '5C', '6H']).rank
assert 5 == rank, "got %s, expected 5" % rank
rank = testSubject.Hand(['AD', 'AC', 'AH', 'KD', 'QD']).rank
assert 4 == rank, "got %s, expected 4" % rank
rank = testSubject.Hand(['AD', 'AC', 'KD', 'KC', 'QH']).rank
assert 3 == rank, "got %s, expected 3" % rank
rank = testSubject.Hand(['AD', 'AC', 'KD', 'QD', 'TD']).rank
assert 2 == rank, "got %s, expected 2" % rank
rank = testSubject.Hand(['AD', 'KC', 'QH', 'JC', '2D']).rank
assert 1 == rank, "got %s, expected 1" % rank


print("TEST EQUAL RANKS")
# royal / straight flush
hand1 = testSubject.Hand(['AD', 'KD', 'QD', 'JD', 'TD'])
hand2 = testSubject.Hand(['2D', '3D', '4D', '5D', '9D'])
assert hand1 > hand2, "hand1 should win"
# four of a kind
hand1 = testSubject.Hand(['AD', 'AC', 'AH', 'AS', 'KD'])
hand2 = testSubject.Hand(['QD', 'QC', 'QH', 'QS', 'KD'])
assert hand1 > hand2, "hand1 should win"
hand1 = testSubject.Hand(['AD', 'AC', 'AH', 'AS', 'KD'])
hand2 = testSubject.Hand(['AD', 'AC', 'AH', 'AS', 'QD'])
assert hand1 > hand2, "hand1 should win"
# full house
hand1 = testSubject.Hand(['AD', 'AC', 'AH', 'KD', 'KC'])
hand2 = testSubject.Hand(['QD', 'QC', 'QH', 'KD', 'KC'])
assert hand1 > hand2, "hand1 should win"
hand1 = testSubject.Hand(['AD', 'AC', 'AH', 'KD', 'KC'])
hand2 = testSubject.Hand(['AD', 'AC', 'AH', 'QD', 'QC'])
assert hand1 > hand2, "hand1 should win"
# Flush
hand1 = testSubject.Hand(['AD', 'KD', 'QD', 'JD', '2D'])
hand2 = testSubject.Hand(['3D', 'KD', 'QD', 'JD', '2D'])
assert hand1 > hand2, "hand1 should win"
# Straight
hand1 = testSubject.Hand(['TC', '9C', '8C', '7C', '6H'])
hand2 = testSubject.Hand(['2C', '3C', '4C', '5C', '6H'])
assert hand1 > hand2, "hand1 should win"
# Three of a kind
hand1 = testSubject.Hand(['AD', 'AC', 'AH', 'KD', 'QD'])
hand2 = testSubject.Hand(['2D', '2C', '2H', 'KD', 'QD'])
assert hand1 > hand2, "hand1 should win"
hand1 = testSubject.Hand(['AD', 'AC', 'AH', 'KD', 'QD'])
hand2 = testSubject.Hand(['AD', 'AC', 'AH', '2D', '3D'])
assert hand1 > hand2, "hand1 should win"
# Two pair
hand1 = testSubject.Hand(['AD', 'AC', 'KD', 'KC', '2H'])
hand2 = testSubject.Hand(['QD', 'QC', 'JD', 'JC', '2H'])
assert hand1 > hand2, "hand1 should win"
hand1 = testSubject.Hand(['AD', 'AC', 'KD', 'KC', '2H'])
hand2 = testSubject.Hand(['AH', 'AS', 'JD', 'JC', '2H'])
assert hand1 > hand2, "hand1 should win"
hand1 = testSubject.Hand(['AD', 'AC', 'KD', 'KC', '3H'])
hand2 = testSubject.Hand(['AH', 'AS', 'KH', 'KS', '2H'])
assert hand1 > hand2, "hand1 should win"
# One pair
hand1 = testSubject.Hand(['AD', 'AC', 'KD', 'QD', 'TD'])
hand2 = testSubject.Hand(['2D', '2C', 'KD', 'QD', 'TD'])
assert hand1 > hand2, "hand1 should win"
hand1 = testSubject.Hand(['AD', 'AC', 'KD', 'QD', 'TD'])
hand2 = testSubject.Hand(['AD', 'AC', '2D', '3D', '4D'])
assert hand1 > hand2, "hand1 should win"
# High card
hand1 = testSubject.Hand(['AD', 'KC', 'QH', 'JC', '2D'])
hand2 = testSubject.Hand(['3D', 'KC', 'QH', 'JC', '2D'])
assert hand1 > hand2, "hand1 should win"

print("TEST EULER EXAMPLE")
with open('example54.txt') as f:
    result = testSubject.main(f)
    assert 3 == result, "got %s, expected 3" % result


print("OFFICIAL EULER FILE")
with open('poker.txt') as f:
    result = testSubject.main(f)
    assert 376 == result, "got %s, expected 376" % result
