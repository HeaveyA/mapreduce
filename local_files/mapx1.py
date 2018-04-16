#!/usr/bin/env python
import sys

for line in sys.stdin:
     cont, num = line.strip().split("\t")
     print('%s\t%s' % (cont, num))