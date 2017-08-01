#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午4:21
# @Author  : C.C
# @File    : demo82.py

# 题目：八进制转换为十进制

if __name__ == '__main__':
    p = input('input a octal number:\n')
    num = 0
    for i in range(len(p)):
        num += 8 ** i * int(p[len(p) - 1 - i])

    print("转换成十进制后是：",num)