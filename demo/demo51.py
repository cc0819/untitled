#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午10:16
# @Author  : C.C
# @File    : demo51.py

# 题目：学习使用按位与 & 。

if __name__ == '__main__':
    a = 5
    b = a & 3
    print('a & b = %d' % b)

    b &= 7
    print('a & b = %d' % b)