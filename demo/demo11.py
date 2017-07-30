#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/30 下午5:50
# @Author  : C.C
# @File    : demo11.py

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

month = int(input("请输入要查的月数:"))
total = 1


def rabbit(num):
    if num == 1 or num == 2 :
        return 1
    else:
        return rabbit(num-1) + rabbit(num-2)


total = rabbit(month)




print("第",month,"月总共有", total * 2, "只兔子")