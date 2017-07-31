#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午5:24
# @Author  : C.C
# @File    : demo27.py

# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


data = []
def res(s, l):
    if l == 0:
        return
    data.append(s[l - 1])
    res(s, l - 1)
    return  data




s = input("请随意输入5个字符：")

print("字符顺序为：", s)


print("字符反序后：", res(s, len(s)))