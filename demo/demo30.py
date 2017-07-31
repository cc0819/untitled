#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午7:03
# @Author  : C.C
# @File    : demo30.py

# 一个5位数，判断它是不是回文数。
# 即12321是回文数，个位与万位相同，十位与千位相同。

number = input("请输入一个正五位数：")


def aguse():
    for i in range(len(number)//2):
        if number[i] != number[-i - 1]:
            return False
            break
        return True

if aguse():
    print ("%s 是一个回文数!" % number)
else:
    print ("%s 不是一个回文数!" % number)