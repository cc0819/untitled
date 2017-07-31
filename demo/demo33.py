#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午7:15
# @Author  : C.C
# @File    : demo33.py

# 题目：按逗号分隔列表。

l = [1, 2, 3, 4, 5]

s = ",".join(str(i) for i in l)


print(s)