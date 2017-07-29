#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/29 下午5:51
# @Author  : C.C
# @File    : demo6.py

# 题目：斐波那契数列。

def fibo(num):
    if num == 1 or num == 2:
        return 1
    return  fibo(num-1) + fibo(num -2)


print(fibo(8))