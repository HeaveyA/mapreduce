#!/usr/bin/env python
import sys

for line in sys.stdin:
     cont, num = city_num_line(line)
     print('%s\t%s' % (cont, num))