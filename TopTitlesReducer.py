#!/usr/bin/env python
import sys

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    count, word = line.split('\t', 1)
    count = int(count)
    print '%s\t%s' % (word, count)
