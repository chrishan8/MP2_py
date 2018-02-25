#!/usr/bin/env python
import sys

leaguePath = sys.argv[1]
leaguePages = []

with open(leaguePath) as f:
	for line in f:
        leaguePages.append(line.strip())

for line in sys.stdin:
    line = line.strip()
    page, count = line.split('\t', 1)
    count = int(count)
    if page in leaguePages:
        print '%s\t%d' % (page, count)
