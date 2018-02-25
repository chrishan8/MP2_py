#!/usr/bin/env python
import sys

currentWord = None
currentTotal = 0

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if currentWord == word:
        currentTotal += count
    else:
        if currentWord:
            print '%s\t%s' % (currentWord, currentTotal)
        currentTotal = count
        currentWord = word

if currentWord == word:
    print '%s\t%s' % (currentWord, currentTotal)
