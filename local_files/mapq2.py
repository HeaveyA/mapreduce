#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    data = line.strip()	
    for data in wordlist:
        print '%s\t%s' % (data)

print '%s\t%s' % (data)