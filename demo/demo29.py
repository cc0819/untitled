#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午6:50
# @Author  : C.C
# @File    : demo29.py

# 给一个不多于5位的正整数，要求：
# 一、求它是几位数，
# 二、逆序打印出各位数字。

number = int(input("请输入一个不多于5位的正整数："))

a = number // 10000
b = number % 10000 // 1000
c = number % 1000 // 100
d = number % 100 // 10
e = number % 10

if a != 0:
    print("5 位数：",e,d,c,b,a)
elif b != 0:
    print("4 位数：",e,d,c,b)
elif c != 0:
    print("3 位数：",e,d,c)
elif d != 0:
    print("2 位数：",e,d)
else:
    print("1 位数：",e)