#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午2:22
# @Author  : C.C
# @File    : demo19.py

# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。

for num in range(2, 1001):
    temp = []
    index = 0
    for j in range(1, num):
        if num % j == 0:
            index += j
            temp.append(j)
    if index == num:
        print(str(sum(temp)), " == ", temp)
