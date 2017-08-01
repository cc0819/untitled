#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午11:49
# @Author  : C.C
# @File    : demo88.py

# 题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

if __name__ == '__main__':
    index = 1

    while index < 8:
        number = int(input("请输入一个(1~50)数字:\n"))
        while number < 1 or number > 50:
            number = int(input("请输入一个(1~50)数字:\n"))

        print(number * "*")
        index += 1
