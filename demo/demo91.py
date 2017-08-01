#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午11:57
# @Author  : C.C
# @File    : demo91.py

# 题目：时间函数举例1。
import time

if __name__ == '__main__':

    print(time.ctime(time.time()))

    print(time.asctime(time.localtime(time.time())))

    print(time.asctime(time.gmtime(time.time())))