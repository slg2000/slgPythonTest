#!/usr/bin/python
#-*- coding: UTF-8 -*-

pyg = 'ay'


original = raw_input('Enter a word:')


if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        new_word = original + 'ay'
        print new_word
    else:
        #print len(original)
        new_word = word[1:]
        new_word = new_word + first + pyg
        print new_word
else:
    print 'empty'
