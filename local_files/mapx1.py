#!/usr/bin/env python
import sys

''' Mapper: Simply, taking in a single pair for both columns 1 (col1) and columns 2 (col2) of the data and outputting all the key value pairs (so, all the instances within the data)
    Also using .strip to remove whitespace and .split("\t") to split the lines based on the tab between the two columns. '''

for line in sys.stdin:
     col1, col2 = line.strip().split("\t")
     print('%s\t%s' % (col1, col2))