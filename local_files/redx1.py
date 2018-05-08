#!/usr/bin/env python

import sys

'''Part A : First, the output from the map phase is sorted and shuffled in the key and val groups and then the key is assigned to 
   finalkey and val to maxval to produce the maximum value.'''

finalkey = None
maxval = None 
for line in sys.stdin:
    key, val = line.strip().split('\t')
    if key != finalkey:
        print('%s\t%s' % (finalkey, maxval))
        maxval = None
    finalkey = key
    maxval = max(val, maxval)
if finalkey:
     print('%s\t%s' % (finalkey, maxval))
