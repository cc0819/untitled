#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午9:17
# @Author  : C.C
# @File    : demo42.py

# 题目：学习使用auto定义变量的用法。

# 变量作用域
num = 2
def autofunc():
    num = 1
    print ('internal block num = %d' % num)
    num += 1

for i in range(3):
    print ('The num = %d' % num)
    num += 1
    autofunc()
