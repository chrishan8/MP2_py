#!/usr/bin/env python
import re
import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
pattern = ''
stopWords = []
linesIn = []

with open(stopWordsPath) as f:
    for line in f:
        stopWords.append(line)

with open(delimitersPath) as f:
    delimiters = f.read().strip()
    pattern = '|'.join(map(re.escape, list(delimiters)))

for line in sys.stdin:
    words = filter(None, map(lambda x: x.strip(), re.split(pattern, line)))
    for word in words:
        word = word.strip().lower()
        if (word not in stopWords):
            print '%s\t%d' % (word, 1)
