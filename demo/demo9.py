#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/30 下午5:34
# @Author  : C.C
# @File    : demo9.py

# 暂停一秒输出。
import time

num = 0
while num < 5:
    print("打印值：", num)
    num += 1
    time.sleep(1)
