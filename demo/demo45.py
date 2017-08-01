#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午9:04
# @Author  : C.C
# @File    : demo45.py

# 题目：统计 1 到 100 之和。

if __name__ == '__main__':
    total = 0
    for i in range(1, 101):
        total += i

    print("求得总和等于：%d" % total)
        