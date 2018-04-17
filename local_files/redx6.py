#!/usr/bin/env python

import sys

sum = None
count = None
ave = None
for line in sys.stdin:
    value = line.strip().split('\t')
    sum = sum(value)
    count = len(value)
    ave = (sum/count)
print (ave)