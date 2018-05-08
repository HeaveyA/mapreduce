#!/usr/bin/env python

from __future__ import division
import sys

#Part B: creating a key (number) and shuffling the data before performing the average calculation (using the built in python tools (import division)).

number = []
for line in sys.stdin:
    number = [int(i) for i in line.strip().split('\t')]
average = sum(number) / len(number)
print(average)