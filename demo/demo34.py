#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午7:15
# @Author  : C.C
# @File    : demo34.py

# 题目：练习函数调用。

def hello_world():
    print ('hello world')

def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
    three_hellos()