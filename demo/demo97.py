#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午6:54
# @Author  : C.C
# @File    : demo97.py

# 题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

if __name__ == '__main__':
    filename = input('输入文件名:\n')
    with open(filename, "a") as fp:
        ch = input('输入字符串:\n')
        while ch != '#':
            fp.write(ch)
            print(ch)
            ch = input('')

