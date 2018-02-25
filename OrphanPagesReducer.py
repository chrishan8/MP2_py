#!/usr/bin/env python
import sys

currentPage = None
currentTotal = 0

for line in sys.stdin:
    line = line.strip()
    try:
        page, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        pass

if currentPage == page:
    currentTotal += count
else:
    if currentPage and currentTotal == 0:
        print '%s' % (currentPage)
    currentTotal = count
    currentPage = page

if currentPage and currentTotal == 0:
print '%s' % (currentPage)
