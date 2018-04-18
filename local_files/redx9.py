#!/usr/bin/env python

import sys
 
distinct_list = []
for each in sys.stdin:
    if each not in distinct_list:
        distinct_list.append(each)
print(distinct_list)