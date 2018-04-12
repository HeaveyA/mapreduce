#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()	
    line = map(int,line)
    for i in line:
        print '%d%d' % (i)

