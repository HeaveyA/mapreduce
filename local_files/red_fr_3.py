#!/usr/bin/env python
import sys

friend_pair = []
for line in sys.stdin:
    values = line.split("\t")
    if not (0 in values):
        x = sum(int(values))
        print (friend_pair, x)