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
average = int(math.floor(len(wordsToCounts) / total))
variance = 0
for (word, count) in wordsToCounts:
    variance += (average - count) ** 2
variance /= len(wordsToCounts)
variance = int(math.floor(variance))

print 'Mean\t%d' % average
print 'Sum\t%d' % total
print 'Min\t%s' % min(wordsToCounts, key=lambda x: x[1])
print 'Max\t%s' % max(wordsToCounts, key=lambda x: x[1])
print 'Var\t%d' % variance
