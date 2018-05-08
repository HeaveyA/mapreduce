#!/usr/bin/env python

import sys

#Part C: Shuffling through the key, pairs from the mapper phase and using .append to find the distinct integers.

unique_list = []
for line in sys.stdin:
	value = line.strip().split('\t')
        if value not in unique_list:
            unique_list.append(value)
print(unique_list)