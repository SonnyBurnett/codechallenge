import solution


def testProcessFileLines():

    expectedLines = ["8C TS KC 9H 4S 7D 2S 5D 3S AC",
                     "5C AD 5D AC 9C 7C 5H 8D TD KS"]

    nrOfLineAssertionsMade = 0

    def stubFunc(line):
        nonlocal nrOfLineAssertionsMade
        nrOfLineAssertionsMade += 1
        assert line == expectedLines.pop(0)

    solution.processFileLines(stubFunc, 'test_input.txt')

    assert nrOfLineAssertionsMade == 2


def testLineToHands():
    line = "2C 3C 4D 9D TD 2H JH QS KS AS"

    assert solution.lineToHands(line) == ("2C 3C 4D 9D TD", "2H JH QS KS AS")


def testScore():
    royalFlush = "TC JC QC KC AC"
    assert solution.score(royalFlush) == (10, 0, 0)

    straightFlush = "2C 3C 4C 5C 6C"
    assert solution.score(straightFlush) == (9, 4, 0)
    assert solution.score(straightFlush) < solution.score(royalFlush)

    fourOfAKind = "2C 2H 2S 2D TC"
    assert solution.score(fourOfAKind) == (8, 0, 8)
    assert solution.score(fourOfAKind) < solution.score(straightFlush)

    fullHouse = "2C 2D 2S 9C 9D"
    assert solution.score(fullHouse) == (7, 0, 7)
    assert solution.score(fullHouse) < solution.score(fourOfAKind)

    flush = "2C 3C 4C 9C TC"
    assert solution.score(flush) == (6, 8, 7)
    assert solution.score(flush) < solution.score(fullHouse)

    straight = "2C 3C 4C 5C 6D"
    assert solution.score(straight) == (5, 4, 0)
    assert solution.score(straight) < solution.score(flush)

    threeOfAKind = "5C 5D 5S 9C TD"
    assert solution.score(threeOfAKind) == (4, 3, 8)
    assert solution.score(threeOfAKind) < solution.score(straight)

    twoPair = "3C 3D 4S 4C TD"
    assert solution.score(twoPair) == (3, 2, 1)
    assert solution.score(twoPair) < solution.score(threeOfAKind)

    pair = "KC KD 4S 9C TD"
    assert solution.score(pair) == (2, 11, 8)
    assert solution.score(pair) < solution.score(twoPair)

    highCard = "AC 3C 4C 9C TD"
    assert solution.score(highCard) == (1, 12, 8)
    assert solution.score(highCard) < solution.score(pair)


def testScoreComparisonToTwoLevelsDeep():
    straightFlush6 = "2C 3C 4C 5C 6C"
    straightFlush10 = "6C 7C 8C 9C TC"
    assert solution.score(straightFlush10) > solution.score(straightFlush6)

    fourOfAKind2 = "2C 2H 2S 2D TC"
    fourOfAKind3 = "3C 3H 3S 3D TC"
    fourOfAKind3HighCardJacks = "3C 3H 3S 3D JD"
    assert solution.score(fourOfAKind3) > solution.score(fourOfAKind2)
    assert solution.score(fourOfAKind3HighCardJacks) > solution.score(fourOfAKind3)

    fullHouse2 = "2C 2D 2S 9C 9D"
    fullHouse3 = "3C 3D 3S 9C 9D"
    fullHouse3and10 = "3C 3D 3S TC TD"
    assert solution.score(fullHouse3) > solution.score(fullHouse2)
    assert solution.score(fullHouse3and10) > solution.score(fullHouse3)

    flush10 = "2C 3C 4C 7C TC"
    flush9 = "2C 3C 4C 7C 9C"
    flush9and8 = "2C 3C 4C 8C 9C"
    assert solution.score(flush10) > solution.score(flush9)
    assert solution.score(flush9and8) > solution.score(flush9)

    straight7 = "3C 4C 5C 6C 7D"
    straight6 = "2C 3C 4C 5C 6D"
    assert solution.score(straight7) > solution.score(straight6)

    threeOfAKind5 = "5C 5D 5S 9C TD"
    threeOfAKind6 = "6C 6D 6S 9C TD"
    threeOfAKind6HighCardKing = "6C 6D 6S 9C KD"
    assert solution.score(threeOfAKind6) > solution.score(threeOfAKind5)
    assert solution.score(threeOfAKind6HighCardKing) > solution.score(threeOfAKind6)

    twoPair4 = "3C 3D 4S 4C TD"
    twoPair5 = "3C 3D 5S 5C TD"
    twoPair5and4 = "4C 4D 4S 4C TD"
    assert solution.score(twoPair5) > solution.score(twoPair4)
    assert solution.score(twoPair5and4) > solution.score(twoPair5)

    pairK = "KC KD 4S 9C TD"
    pairA = "AC AD 4S 9C TD"
    pairAHighCardJ = "AC AD 4S 9C JD"
    assert solution.score(pairA) > solution.score(pairK)
    assert solution.score(pairAHighCardJ) > solution.score(pairA)

    highCardT = "2C 3C 4C 9C TD"
    highCardA = "2C 3C 4C 9C AD"
    highCardAHighCard10 = "2C 3C 4C TC AD"
    assert solution.score(highCardA) > solution.score(highCardT)
    assert solution.score(highCardAHighCard10) > solution.score(highCardA)


def testExerciseTestCases():
    assert solution.score("5H 5C 6S 7S KD") < solution.score("2C 3S 8S 8D TD")
    assert solution.score("5D 8C 9S JS AC") > solution.score("2C 5C 7D 8S QH")
    assert solution.score("2D 9C AS AH AC") < solution.score("3D 6D 7D TD QD")
    assert solution.score("4D 6S 9H QH QC") > solution.score("3D 6D 7H QD QS")
    assert solution.score("2H 2D 4C 4D 4S") > solution.score("3C 3D 3S 9S 9D")
