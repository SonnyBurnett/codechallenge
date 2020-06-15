def processFileLines(func, file):
    with open(file) as f:
        for line in f:
            func(line.rstrip())
