#!/usr/bin/env python

import sys
 
unique_list = []
for line in sys.stdin:
	value = line.strip().split('\t')
    if line not in unique_list:
        unique_list.append(value)
print(unique_list)