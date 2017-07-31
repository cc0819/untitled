#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午2:23
# @Author  : C.C
# @File    : demo23.py

# 打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
from sys import stdout

number = int(input("请输入大于1的要打印的雪花数："))



def pr(num):
    # 上半部分
    for i in range(num):
        for a in range(num - i):  # 输出空格
            stdout.write(' ')
        for b in range(2 * i + 1):  # 输出*
            stdout.write('*')

    # 下半部分
    for j in range(num - 1):
        for c in range(num):  # 输出空格
            stdout.write(' ')
        for d in range(num):  # 输出*
            stdout.write('*')


pr(number)