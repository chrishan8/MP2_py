#!/usr/bin/env python
import sys

wordsToCounts = []

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)
    wordsToCounts.append((word, count))

total = 0
for (word, count) in wordsToCounts:
    total += count
average = len(wordsToCounts) / total
for (word, count) in wordsToCounts:
    variance += (average - count) ** 2
variance /= len(wordsToCounts)

print 'Mean\t%d' % average
print 'Sum\t%d' % total
print 'Min\t%d' % min(wordsToCounts, key=lambda x: x[1])
print 'Max\t%d' % max(wordsToCounts, key=lambda x: x[1])
print 'Var\t%d' % variance
