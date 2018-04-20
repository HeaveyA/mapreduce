#!/usr/bin/env python
import sys

friend_pair = []
for line in sys.stdin:
    values = line.split("\t")
    if not (0 in values):
        print (friend_pair, sum(values))