#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午11:59
# @Author  : C.C
# @File    : demo92.py

# 题目：时间函数举例2。
import time

if __name__ == '__main__':


    start = time.time()

    for i in range(10):
        print(i)

    end = time.time()


    print(end - start)