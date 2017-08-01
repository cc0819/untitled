#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午4:49
# @Author  : C.C
# @File    : demo68.py

# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

if __name__ == '__main__':
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = 4
    for i in range(m):
        number.insert(0, number.pop())
    print(number)