#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/29 下午12:22
# @Author  : C.C
# @File    : demo5.py

# 输入三个整数x,y,z，请把这三个数由小到大输出。

num = []

for inputNum in range(0,3):
    temp = input("输入的Integer:\n")
    num.append(temp)

num.sort()
# num.sort(reverse=True)
print("排序后是：",num)
