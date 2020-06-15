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


def testParseLineToHands():
    line = "2C 3C 4D 9D 10D 2H JH QS KS AS"

    assert solve.parseLineToHands(line) == ([(2, 'C'), (3, 'C'), (4, 'D'), (9, 'D'), (10, 'D')],
                                            [(2, 'H'), (11, 'H'), (12, 'S'), (13, 'S'), (14, 'S')])


def testScore():
    fourOfAKind = [(2, 'C'), (2, 'C'), (2, 'C'), (2, 'C'), (10, 'C')]
    assert solve.score(fourOfAKind) == 8

    flush = [(2, 'C'), (3, 'C'), (4, 'C'), (9, 'C'), (10, 'C')]
    assert solve.score(flush) == 6

    highCard = [(2, 'C'), (3, 'C'), (4, 'C'), (9, 'C'), (10, 'D')]
    assert solve.score(highCard) == 1
