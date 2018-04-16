#!/usr/bin/env python
import sys

max = 0
for line in sys.stdin:
    fields = line.strip().split(",")
    if fields.isdigit():
        val = int(fields)
        if (val > max):
            max = val
        else:
                print max