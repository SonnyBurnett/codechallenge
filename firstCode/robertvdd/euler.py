#!/usr/bin/env python
import time, sys
from os import path

sys.path.append("./solutions")

if len(sys.argv) != 2:
    print("Please provide a problem number as argument. Usage: ./euler.py 1")
    exit(-1)
else:
    filename = "solutions/%s.py" % sys.argv[1]

start_time = time.time()
exec(open(filename).read())
duration = time.time() - start_time

print("Duration: %f seconds." % duration)

