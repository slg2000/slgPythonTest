#!/usr/bin/python
'''
usage: 

./download.py http://www1.pconline.com.cn/2010/dl/add/images/dlLogo.png savename.png
Readme:
first parameter:target for download
second parameter: rename the download target

'''
import urllib, sys

f = urllib.urlopen(sys.argv[1])

myfile = open(sys.argv[2], 'wa')

while 1:
    buf = f.read(2048)
    if not len(buf):
        break
    myfile.write(buf)
