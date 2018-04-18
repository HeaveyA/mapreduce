#!/usr/bin/env python

import sys
 
unique_list = []
for line in sys.stdin:
    if line not in unique_list:
        unique_list.append(line)
print(unique_list)