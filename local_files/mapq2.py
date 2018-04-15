#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()	
    for i in line:
        print '%s' % (i)

