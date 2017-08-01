#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午7:18
# @Author  : C.C
# @File    : demo_plus.py

# 题目： 获取 100 以内的质数。

if __name__ == '__main__':

    num = []

    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            num.append(i)

    print(num)
