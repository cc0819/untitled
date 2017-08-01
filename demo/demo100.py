#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午1:38
# @Author  : C.C
# @File    : demo100.py

# 题目：列表转换为字典。

a = ["name", "age", "sex"]

b = ["张三", 9, "male"]

print(dict(zip(a,b)))
