#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午1:23
# @Author  : C.C
# @File    : demo96.py

# 题目：计算字符串中子串出现的次数。


if __name__ == '__main__':
    str1 = input('请输入一个字符串:\n')
    str2 = input('输入要判断的字符串:\n')
    count = str1.count(str2)
    print(count)