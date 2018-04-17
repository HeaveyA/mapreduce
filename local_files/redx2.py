#!/usr/bin/env python

import sys

sum_risk = None
count = None
ave = None
for line in sys.stdin:
    value = line.strip().split('\t')
    sum_risk += value
    count += 1
    ave = (sum_risk/count)
print (ave)