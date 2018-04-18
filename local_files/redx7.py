#!/usr/bin/env python

import sys
 
value=[]
for line in sys.stdin:
    value = line(set(value))
print (value)

