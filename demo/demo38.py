#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午7:46
# @Author  : C.C
# @File    : demo38.py

# 求一个3*3矩阵对角线元素之和。

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

total = 0

for i in range(0,3):
    total += matrix[i][i]


print("对角线之和 %d" %total)

