#!/usr/bin/env python
import sys

for line in sys.stdin:
    def mapper(key, value):
        key = 0
        print key, max(value)