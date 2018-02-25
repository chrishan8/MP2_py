#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
    links = filter(None, re.split(r'[ :]', line))
    links.pop(0)
    for link in links:
        print '%s\t%d' % (link, 1)
