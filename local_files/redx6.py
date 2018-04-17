#!/usr/bin/env python

import sys



ave = []
for line in sys.stdin:
    value = [int(n) for n in line.strip().split('\t')]
    sum = sum(value)
    count = len(value)
    ave = (sum/count)
print (ave)