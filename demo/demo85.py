#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午7:21
# @Author  : C.C
# @File    : demo85.py

# 题目：输入一个正整数，然后判断最少几个 9 除于该数的结果为整数。
# 程序分析：999999 / 13 = 76923。

if __name__ == '__main__':
    number = int(input('输入一个数字:\n'))
    a = 9
    n = 1
    # index = 0
    while True:
        # print(index)
        if a % number == 0:
            break
        else:
            a = a * 10 + 9
            n += 1
        # index += 1

    print('%d 个 9 除于 %d 为整数' % (n,number))