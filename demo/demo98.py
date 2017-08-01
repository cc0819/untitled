#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午7:04
# @Author  : C.C
# @File    : demo98.py

# 题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，
# 然后输出到一个磁盘文件"test"中保存。


if __name__ == '__main__':
    str = input('please input a string:\n')
    with open("text.txt", "w") as temp:
        temp.write(str.upper())

    with open("text.txt") as read:
        print(read.read())
