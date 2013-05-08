#!/usr/bin/python
#-*- coding: UTF-8 -*-

'''
算法思想：对于一个单词，
   如果第一个字母是元音开头的，在单词末尾加'ay'，
   如果第一个字母是辅员开后的，将第一个字每移到末尾，然后在末尾加'ay'，
   如：
	输入python,结果为　ythonpay.
	输入apple,结果为 appleay.
'''

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
