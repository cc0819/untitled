#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/30 下午5:36
# @Author  : C.C
# @File    : demo10.py

# 暂停一秒输出，并格式化当前时间。
import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


time.sleep(1)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))