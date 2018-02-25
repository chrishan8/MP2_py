#!/usr/bin/env python
import re
import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
pattern = ''
stopWords = []

with open(stopWordsPath) as f:
    for line in f:
        stopWords.append(line)

with open(delimitersPath) as f:
    delimiters = f.read().strip()
    pattern = '|'.join(map(re.escape, list(delimiters)))

for line in sys.stdin:
    words = filter(None, re.split(pattern, line))
    for word in words:
        word = word.strip().lower()
        if (word not in stopWords):
            print '%s\t%s' % (word, '1')
