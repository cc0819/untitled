#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午12:12
# @Author  : C.C
# @File    : demo95.py

# 题目：字符串日期转换为易读的日期格式。
import time

dt = "2017-05-05 20:28:54"

timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")

print(timeArray)

timestamp = time.mktime(timeArray)

print(timestamp)

dt_new = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

print(dt_new)
