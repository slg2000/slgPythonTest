#!/usr/bin/python
#-*- coding: UTF-8 -*-
'''
返回列表中的中间值，如果是偶数的话，取中间两个值的合的平均值
'''
def median(ln):
    new_ln = sorted(ln)
    print new_ln
    count = 0
    if 0 != len(new_ln) % 2:
        print "enter if"
        count = len(new_ln) / 2 + 1
        return new_ln[count-1]
    else:
        print "enter else"
        count = len(new_ln) / 2
        return (new_ln[count-1] + new_ln[count]) / 2.0


print median([4,5,5,4])
