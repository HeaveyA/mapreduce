#!/usr/bin/env python

import sys
 
value=[]
for line in sys.stdin:
    value = (set(line))
print (value)

