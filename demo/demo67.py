#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午4:54
# @Author  : C.C
# @File    : demo67.py

# 题目：输入数组，最大的与第一个元素交换，
# 最小的与最后一个元素交换，输出数组。

if __name__ == '__main__':
    number = [2, 3, 7, 1, 9, 8, 5, 16]
    print(number)

    max = max(number)
    max_index = number.index(max)
    number[max_index], number[0] = number[0], number[max_index]

    print("最大交换后为:", number)

    min = min(number)
    min_index = number.index(min)
    number[min_index], number[len(number) - 1] = number[len(number) - 1], number[min_index]


    print("最小交换后为:", number)
