#!/usr/bin/env python

import sys
from __future__ import division

num = []
for line in sys.stdin:
    num = [int(n) for n in line.strip().split('\t')]
avg = sum(num) / len (num)
print(avg)