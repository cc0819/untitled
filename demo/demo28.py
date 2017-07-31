#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午6:43
# @Author  : C.C
# @File    : demo28.py

# 有5个人坐在一起，
# 问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？


def age(num):
    if num == 1 :
        c = 10
    else:
        c = age(num - 1) + 2

    return c

print("第五个人的年龄为：", age(5))