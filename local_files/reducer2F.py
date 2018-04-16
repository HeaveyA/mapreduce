#!/usr/bin/env python 
# map1.py

import sys

last_key = None
for line in sys.stdin:
    key = line.strip().split('\t')
    if key != last_key:
        print('%s\t' % (last_key))
        max_key = None
    last_key = key
    max_key = max(max_key)
if last_key:
     print('%s\t' % (last_key))