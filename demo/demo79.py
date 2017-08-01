#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午11:22
# @Author  : C.C
# @File    : demo79.py

# 题目：字符串排序。

if __name__ == '__main__':
    str = ["e", "f", "c", "d"]

    print("before=", str)

    for i in range(len(str) - 1):
        for j in range(len(str) - i - 1):
            if str[j] > str[j + 1]:
                str[j], str[j + 1] = str[j + 1], str[j]

    print("before=", str)
