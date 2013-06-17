#encoding:utf-8
#!/usr/bin/python
#-*- coding: UTF-8 -*-
choice = raw_input('Enjoying the course? (y/n)')
print choice

if choice != "y" and choice != "n":# Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")
    print "your input is :"+choice
