#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午7:37
# @Author  : C.C
# @File    : demo36.py

# 题目：求100之内的素数。

lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

number = 0
data = []
for m in range(lower, upper + 1):
    if m > 1:
        for i in range(2, m // 2 ):
            if m % i == 0:
                break
        else:
            number += 1
            data.append(m)


print("%s到%s素数总数为%d" % (lower, upper, number))
print("分别是", data)