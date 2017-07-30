#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/30 下午5:20
# @Author  : C.C
# @File    : demo8.py

# 输出 9*9 乘法口诀表。

for i in range(1, 10):
    print()
    for j in range(1, i + 1):
        print("{} * {} = {}".format(i, j, i * j),'\t', end="")