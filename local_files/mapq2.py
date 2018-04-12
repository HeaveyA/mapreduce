#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    data = line.strip[0:5]	
    data2 = map(int,data)
    for i in data2:
        print '%d' % (i)

