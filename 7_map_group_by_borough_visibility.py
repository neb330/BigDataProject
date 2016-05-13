#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    result = line.split(",")
    if 'dewpoint' not in result and 'borough' not in result:
        borough = result[1]
        visibility = result[41]
        print '%s\t%s' % (borough, visibility)
        