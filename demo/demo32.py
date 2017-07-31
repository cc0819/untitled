#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午7:14
# @Author  : C.C
# @File    : demo32.py

# 按相反的顺序输出列表的值。

a = ['one', 'two', 'three']
a.reverse()
print("直接操作列表", a)

for i in a[::-1]:
    print(i)