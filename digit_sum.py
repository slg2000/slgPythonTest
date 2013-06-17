#!/usr/bin/python
#-*- coding: UTF-8 -*-
def digit_sum(i_num):
    total = 0 
    length = len(str(i_num))
    for i in range(length):
        total += i_num / 10**i % 10
        i += 1
    return total

i_num = 12345
print digit_sum(i_num)
