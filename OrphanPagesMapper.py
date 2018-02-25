#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
    links = filter(None, map(lambda x: x.strip(), re.split(r'[ :]', line)))
    parent = links.pop(0)
    print '%s\t%d' % (parent, 0)
    for child in links:
        print '%s\t%s' % (child, 1)
