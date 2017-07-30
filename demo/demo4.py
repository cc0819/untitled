#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/30 下午6:04
# @Author  : C.C
# @File    : demo4.py

# 输入某年某月某日，判断这一天是这一年的第几天？
import time

print(time.strftime("%Y", time.localtime(time.time())))

year = int(input('year:\n'))

month = int(input('month:\n'))

day = int(input('day:\n'))

total = 0
two_month = 0
big_month = [1, 3, 5, 7, 8, 10, 12]

if month > 2:
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        two_month = 29
    else:
        two_month = 28

total += two_month

for index in range(1, month):
    if index == 2: continue
    if index in big_month:
        total += 31
    else:
        total += 30
    index += 1

total += day

print(year, '年', month, '月', day, '日,是这一年的第', total, '天！')
