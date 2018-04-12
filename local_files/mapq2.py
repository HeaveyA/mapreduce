#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    data = line.strip()	
    for i in data:
        print '%d' % (i)

