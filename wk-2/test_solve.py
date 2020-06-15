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
    assert solve.score(royalFlush) == 10

    straightFlush = "2C 3C 4C 5C 6C"
    assert solve.score(straightFlush) == 9

    fourOfAKind = "2C 2H 2S 2D TC"
    assert solve.score(fourOfAKind) == 8

    fullHouse = "2C 2D 2S 9C 9D"
    assert solve.score(fullHouse) == 7

    flush = "2C 3C 4C 9C TC"
    assert solve.score(flush) == 6

    straight = "2C 3C 4C 5C 6D"
    assert solve.score(straight) == 5

    threeOfAKind = "2C 2D 2S 9C TD"
    assert solve.score(threeOfAKind) == 4

    twoPair = "2C 2D 4S 4C TD"
    assert solve.score(twoPair) == 3

    pair = "2C 2D 4S 9C TD"
    assert solve.score(pair) == 2

    highCard = "2C 3C 4C 9C TD"
    assert solve.score(highCard) == 1
