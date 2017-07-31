#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午7:46
# @Author  : C.C
# @File    : demo39.py

# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

if __name__ == '__main__':
    number = [3, 1, 60, 24, 21, 27, 30, 50, 78, 11]
    num = int(input("请输入要插入的数字："))
    number.append(num)

    for i in range(0,len(number)):
        for j in range(i + 1,len(number)):
            if number[i] > number[j]:
                number[i], number[j] = number[j], number[i]

    print("排序后为%s" %number)