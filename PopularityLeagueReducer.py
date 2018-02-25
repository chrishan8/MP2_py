#!/usr/bin/env python
import sys

pagesToCounts = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    try:
        page, count = line.split('\t', 1)
        count = int(count)
        pagesToCounts.append((page, count))
    except ValueError:
        pass

pagesToCounts = sorted(pagesToCounts, key=lambda x: x[1])
pagesToRank = []
for i in len(pagesToCounts):
    page, count = pagesToCounts[i]
    pagesToRank.append((page, i))

for (page, rank) in sorted(pagesToRank, key=lambda x: x[0])
    print '%s\t%d' % (page, rank)
