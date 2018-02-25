#!/usr/bin/env python
import re
import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
delimters = ''
stopWords = []

with open(stopWordsPath) as f:
    for line in f:
        stopWords.append(line)

with open(delimitersPath) as f:
    delimiters = f.read()

for line in sys.stdin:
    pattern = '|'.join(list(delimiters))
    words = re.split(pattern, line)
    for word in words:
        word = word.strip().lower()
        if (word not in stopWords):
            print '%s\t%d' % (word, 1)
