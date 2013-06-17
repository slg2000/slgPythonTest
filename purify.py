#!/usr/bin/python
'''
ex:
print purify([1,2,3,4])
[2,4]    
'''

def purify(ln):
    length = len(ln)
    new_ln = []
    for i in range(length):
        if ln[i] % 2 == 0:
            new_ln.append(ln[i])
    return new_ln

print purify([3,4,5,6,7,8,10])

