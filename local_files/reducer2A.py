#!/usr/bin/env python 
# map1.py

import sys

for line in sys.stdin: 
    keyval=line.strip().split("\t")
    key,val=(keyval[0],keyval[0])
    global_max = 0
    for value in val:
            if (value > global_max):
                global_max = value
            print(global_max)
           
	