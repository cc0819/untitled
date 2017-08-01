#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午11:11
# @Author  : C.C
# @File    : demo73.py

# 题目：反向输出一个链表。


if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    print(ptr)
    ptr.reverse()
    print(ptr)