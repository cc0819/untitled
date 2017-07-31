#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午5:05
# @Author  : C.C
# @File    : demo25.py

# 求1+2!+3!+...+20!的和。

start = 1
total = 0

for index in range(1, 21):
    start *= index
    total += start

print("求1+2!+3!+...+20! = %d" % total)