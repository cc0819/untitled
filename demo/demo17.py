#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/30 下午11:09
# @Author  : C.C
# @File    : demo17.py

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

s = input("input a string :")

英文 = 0
空格 = 0
数字 = 0
其他 = 0

for i in s:
    if i.isalpha():
        英文 += 1
    elif i.isspace():
        空格 += 1
    elif i.isnumeric():
        数字 += 1
    else:
        其他 += 1
print('英文 = %s,空格 = %s,数字 = %s,其他 = %s' % (英文, 空格, 数字, 其他))
