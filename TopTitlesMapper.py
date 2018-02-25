#!/usr/bin/env python
import sys

wordsToCounts = []

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)
    wordsToCounts.append((word, count))

wordsToCounts = sorted(wordsToCounts, key=lambda x: (x[1], x[0]))
for x in range(5):
    word, count = wordsToCounts.pop()
    print '%s\t%s' % (word, count)
