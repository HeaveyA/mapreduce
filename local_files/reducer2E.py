#!/usr/bin/env python 
# map1.py

import sys

last_key = None
max_val = None 
for line in sys.stdin:
    keyval = line.strip().split('\t')
    if keyval != last_key:
        print('%s\t%s' % (last_key, max_val))
        max_val = None
    last_key = keyval
    max_val = max(keyval, max_val)
if last_key:
     print('%s\t%s' % (last_key, max_val))