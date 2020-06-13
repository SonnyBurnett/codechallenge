import solve


def testProcessFileLines():

    expectedLines = ["8C TS KC 9H 4S 7D 2S 5D 3S AC\n",
                     "5C AD 5D AC 9C 7C 5H 8D TD KS\n"]

    def stubFunc(line):
        assert line == expectedLines.pop(0)

    solve.processFileLines(stubFunc, 'test_input.txt')
