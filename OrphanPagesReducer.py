#!/usr/bin/env python
import sys

currentPage = None
currentTotal = 0
orphanPages = []

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
            orphanPages.append(currentPage)
        currentTotal = count
        currentPage = page

if currentPage and currentTotal == 0:
	orphanPages.append(currentPage)

for page in sorted(orphanPages, key=lambda x: int(x)):
    print page
