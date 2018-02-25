#!/usr/bin/env python
import sys

currentPage = None
currentTotal = 0

# input comes from STDIN
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
        if currentPage:
            print '%s\t%s' % (currentPage, currentTotal)
        currentTotal = count
        currentPage = page

if currentPage == page:
    print '%s\t%s' % (currentPage, currentTotal)
