#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午8:57
# @Author  : C.C
# @File    : demo47.py

# 题目：两个变量值互换。

def change(x, y):
    x, y = y, x
    print("x = %d, y = %d" % (x, y))


if __name__ == '__main__':
    x = 10
    y = 20
    change(x,y)