#!/usr/bin/env python 
# map1.py

import sys

last_key = None
max_val = None 
for line in sys.stdin:
    key, val = line.strip().split('\t')
    if key != last_key:
        print('%s\t' % (last_key))
        max_val = None
    last_key = key
    max_val = max(val, max_val)
if last_key:
     print('%s\t' % (max_val))