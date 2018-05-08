#!/usr/bin/env python

import sys

#Part D: Shuffling through the key pairs from the mapper phase and using .append to find the distinct integers before retrieving the count using 'len'

unique_list = []
for line in sys.stdin:
    if line not in unique_list:
        unique_list.append(line)
print(len(unique_list))