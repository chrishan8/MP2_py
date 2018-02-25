#!/usr/bin/env python
import sys

pagesToCounts = []

for line in sys.stdin:
    line = line.strip()
    page, count = line.split('\t', 1)
    count = int(count)
    pagesToCounts.append((page, count))

pagesToCounts = sorted(pagesToCounts, key=lambda x: (x[1], x[0]))
for x in range(5):
    page, count = pagesToCounts.pop()
    print '%s\t%d' % (page, count)
