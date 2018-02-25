#!/usr/bin/env python
import sys

countsToWords = []

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)
    countsToWords.append((word, count))

countsToWords = sorted(countsToWords, key=lambda x: (x[1], x[0]))
for x in range(10):
    item = countsToWords.pop()
    print '%s\t%s' % (item[0], item[1])
