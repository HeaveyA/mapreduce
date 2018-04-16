#!/usr/bin/env python
import sys

last_key = None
max_val = None 
for line in sys.stdin:
    key, val = line.strip().split('\t')
    if key != last_key:
        print('%s\t%s' % (last_key, max_val))
        max_val = None
    last_key = key
    max_val = max(val, max_val)
if last_key:
     print('%s\t%s' % (last_key, max_val))
