#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午5:19
# @Author  : C.C
# @File    : demo26.py

# 题目：利用递归方法求5!

def plus(num):
    total = 0
    if num == 0 or num == 1:
        total = 1
    else:
        total = num * plus(num - 1)

    return total

print("递归方法求5!", plus(5))