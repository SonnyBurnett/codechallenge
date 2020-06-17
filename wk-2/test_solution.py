import solve


def testProcessFileLines():

    expectedLines = ["8C TS KC 9H 4S 7D 2S 5D 3S AC",
                     "5C AD 5D AC 9C 7C 5H 8D TD KS"]

    nrOfLineAssertionsMade = 0

    def stubFunc(line):
        nonlocal nrOfLineAssertionsMade
        nrOfLineAssertionsMade += 1
        assert line == expectedLines.pop(0)

    solve.processFileLines(stubFunc, 'test_input.txt')

    assert nrOfLineAssertionsMade == 2


def testLineToHands():
    line = "2C 3C 4D 9D TD 2H JH QS KS AS"

    assert solve.lineToHands(line) == ("2C 3C 4D 9D TD", "2H JH QS KS AS")


def testScore():
    royalFlush = "TC JC QC KC AC"
    assert solve.score(royalFlush) == (10, 0, 0)

    straightFlush = "2C 3C 4C 5C 6C"
    assert solve.score(straightFlush) == (9, 4, 0)
    assert solve.score(straightFlush) < solve.score(royalFlush)

    fourOfAKind = "2C 2H 2S 2D TC"
    assert solve.score(fourOfAKind) == (8, 0, 8)
    assert solve.score(fourOfAKind) < solve.score(straightFlush)

    fullHouse = "2C 2D 2S 9C 9D"
    assert solve.score(fullHouse) == (7, 0, 7)
    assert solve.score(fullHouse) < solve.score(fourOfAKind)

    flush = "2C 3C 4C 9C TC"
    assert solve.score(flush) == (6, 8, 7)
    assert solve.score(flush) < solve.score(fullHouse)

    straight = "2C 3C 4C 5C 6D"
    assert solve.score(straight) == (5, 4, 0)
    assert solve.score(straight) < solve.score(flush)

    threeOfAKind = "5C 5D 5S 9C TD"
    assert solve.score(threeOfAKind) == (4, 3, 8)
    assert solve.score(threeOfAKind) < solve.score(straight)

    twoPair = "3C 3D 4S 4C TD"
    assert solve.score(twoPair) == (3, 2, 1)
    assert solve.score(twoPair) < solve.score(threeOfAKind)

    pair = "KC KD 4S 9C TD"
    assert solve.score(pair) == (2, 11, 8)
    assert solve.score(pair) < solve.score(twoPair)

    highCard = "AC 3C 4C 9C TD"
    assert solve.score(highCard) == (1, 12, 8)
    assert solve.score(highCard) < solve.score(pair)


def testScoreComparisonToTwoLevelsDeep():
    straightFlush6 = "2C 3C 4C 5C 6C"
    straightFlush10 = "6C 7C 8C 9C TC"
    assert solve.score(straightFlush10) > solve.score(straightFlush6)

    fourOfAKind2 = "2C 2H 2S 2D TC"
    fourOfAKind3 = "3C 3H 3S 3D TC"
    fourOfAKind3HighCardJacks = "3C 3H 3S 3D JD"
    assert solve.score(fourOfAKind3) > solve.score(fourOfAKind2)
    assert solve.score(fourOfAKind3HighCardJacks) > solve.score(fourOfAKind3)

    fullHouse2 = "2C 2D 2S 9C 9D"
    fullHouse3 = "3C 3D 3S 9C 9D"
    fullHouse3and10 = "3C 3D 3S TC TD"
    assert solve.score(fullHouse3) > solve.score(fullHouse2)
    assert solve.score(fullHouse3and10) > solve.score(fullHouse3)

    flush10 = "2C 3C 4C 7C TC"
    flush9 = "2C 3C 4C 7C 9C"
    flush9and8 = "2C 3C 4C 8C 9C"
    assert solve.score(flush10) > solve.score(flush9)
    assert solve.score(flush9and8) > solve.score(flush9)

    straight7 = "3C 4C 5C 6C 7D"
    straight6 = "2C 3C 4C 5C 6D"
    assert solve.score(straight7) > solve.score(straight6)

    threeOfAKind5 = "5C 5D 5S 9C TD"
    threeOfAKind6 = "6C 6D 6S 9C TD"
    threeOfAKind6HighCardKing = "6C 6D 6S 9C KD"
    assert solve.score(threeOfAKind6) > solve.score(threeOfAKind5)
    assert solve.score(threeOfAKind6HighCardKing) > solve.score(threeOfAKind6)

    twoPair4 = "3C 3D 4S 4C TD"
    twoPair5 = "3C 3D 5S 5C TD"
    twoPair5and4 = "4C 4D 4S 4C TD"
    assert solve.score(twoPair5) > solve.score(twoPair4)
    assert solve.score(twoPair5and4) > solve.score(twoPair5)

    pairK = "KC KD 4S 9C TD"
    pairA = "AC AD 4S 9C TD"
    pairAHighCardJ = "AC AD 4S 9C JD"
    assert solve.score(pairA) > solve.score(pairK)
    assert solve.score(pairAHighCardJ) > solve.score(pairA)

    highCardT = "2C 3C 4C 9C TD"
    highCardA = "2C 3C 4C 9C AD"
    highCardAHighCard10 = "2C 3C 4C TC AD"
    assert solve.score(highCardA) > solve.score(highCardT)
    assert solve.score(highCardAHighCard10) > solve.score(highCardA)


def testExerciseTestCases():
    assert solve.score("5H 5C 6S 7S KD") < solve.score("2C 3S 8S 8D TD")
    assert solve.score("5D 8C 9S JS AC") > solve.score("2C 5C 7D 8S QH")
    assert solve.score("2D 9C AS AH AC") < solve.score("3D 6D 7D TD QD")
    assert solve.score("4D 6S 9H QH QC") > solve.score("3D 6D 7H QD QS")
    assert solve.score("2H 2D 4C 4D 4S") > solve.score("3C 3D 3S 9S 9D")
