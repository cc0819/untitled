#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午2:23
# @Author  : C.C
# @File    : demo24.py

# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
# 求出这个数列的前20项之和。


total = 0
a, b = 2, 1

for i in range(1, 21):
    total += a / b
    a, b = a + b, a

print("前20项的之和是：%s" % total)