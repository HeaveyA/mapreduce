#!/usr/bin/env python

import sys
 
distinct_list = []
for line in sys.stdin:
    if line not in unique_list:
        unique_list.append(line)
print(distinct_list)