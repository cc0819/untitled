#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/28 下午12:08
# @Author  : C.C
# @File    : demo3.py

# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

for m in range(168):
    for n in range(m):
        if (m + n) * (m - n) == 168:
            x = n ** 2 - 100
            print("符合条件的整数有:", x)
