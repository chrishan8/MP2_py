#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
    links = filter(None, map(lambda x: x.strip(), re.split(r'[ :]', line)))
    links.pop(0)
    for link in links:
        print '%s\t%s' % (link, 1)
