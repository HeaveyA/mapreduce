#!/usr/bin/env python

import sys

sum = None
count = None
ave = None
for line in sys.stdin:
    value = line.strip().split('\t')
    sum += value
    count += 1
    ave = (sum/count)
print (ave)