#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午8:50
# @Author  : C.C
# @File    : demo46.py

# 求输入数字的平方，如果平方运算后小于 50 则退出。

number = int(input("请输入一个数字："))

def operation(number):
    end = number ** 2
    if end < 50:
        return False
    return True




if operation(number):
    print("输入数字的平方数是：", number ** 2)
else:
   print ('如果输入的数字小于 50，程序将停止运行。')