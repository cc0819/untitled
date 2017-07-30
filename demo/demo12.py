#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/30 下午10:41
# @Author  : C.C
# @File    : demo12.py

# 判断101-200之间有多少个素数，并输出所有素数。

num = []
index = 0
for i in range(101, 201):
    for m in range(2, i):
        if i % m == 0:
            break
    else:
        index += 1
        num.append(i)

print("101-200之间有", index, "个素数", "\n分别是", num)
