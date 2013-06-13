#!/usr/bin/python
import socket,sys
'''
Try to excute this program as follow:
    network_1_client.py quux.org /
And the program will try to get the file list in quux.org/
'''

port = 70
host = sys.argv[1]      #argv[1] is the first input  parameter when excute this program
filename = sys.argv[2]  #argv[2] is the second input parameter when excute this program
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
except socket.gaierror,e:
    print "Error connecting to server: %s" % e
    sys.exit(1)

s.sendall(filename + "\r\n")

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
