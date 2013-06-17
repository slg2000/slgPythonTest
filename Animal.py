#!/usr/bin/python

class Animal(object):
    is_alive = True
    health = "good"
    def __init__(self, name, age):
		self.name = name
		self.age = age
	# Add your method here!
    def description():
        print "name:"+self.name
        print "age:"+self.age

hippo = Animal("sddd",30)
sloth = Animal("sloth",22)
ocelot = Animal("ocelot",33)
print hippo.health
print sloth.health
print ocelot.health
