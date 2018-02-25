#!/usr/bin/env python

import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
delimters = ""
stopWords = []

with open(stopWordsPath) as f:
    for line in f:
        stopWords.append(line)

with open(delimitersPath) as f:
    delimiters = f.read()

for line in sys.stdin:
    words = line.split(delimiters)
    for word in words:
        word.strip().lower()
        print '%s\t%s' % (word, 1)
