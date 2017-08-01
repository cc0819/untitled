#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午9:23
# @Author  : C.C
# @File    : demo66.py

# 题目：输入3个数a,b,c，按大小顺序输出。

if __name__ == '__main__':
    number = []

    for i in range(3):
        number.append(int(input("请输入一个数字：")))


    number.sort()


    print(number)


