#!/usr/bin/python
import urllib, sys

address = sys.argv[1]

f = urllib.urlopen(address)
for line in f.readlines():
    sys.stdout.write(line)
