#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午10:21
# @Author  : C.C
# @File    : demo54.py

# 题目：取一个整数a从右端开始的4〜7位。
# 程序分析：可以这样考虑：
# (1)先使a右移4位。
# (2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
# (3)将上面二者进行&运算。

if __name__ == '__main__':
    number = int(input("输入数字："))
    b = number >> 4
    c = ~(~0 << 4)
    d = b & c
    print('%o\t%o' % (number, d))
