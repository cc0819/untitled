#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午11:59
# @Author  : C.C
# @File    : demo92.py

# 题目：时间函数举例3。
import time

if __name__ == '__main__':

    start = time.clock()

    for i in range(10000):
        print(i)

    end = time.clock()

    print("%6.3f" % (end - start))
    print("%1.3f" % 2.7)
    print("%3.3f" % 2.7)
