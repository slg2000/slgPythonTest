#!/usr/bin/python
def remove_duplicates(ln):
    new_ln = []
    length = len(ln)
    for i in range(length):
        new_length = len(new_ln)
        count = 0
        for j in range(new_length):
            if new_ln[j] == ln[i]:
                count += 1
        if count == 0:
            new_ln.append(ln[i])
    return new_ln

print remove_duplicates([1,3,1,1,4,5,4,6,9,9])

