#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/3 下午5:56
# @Author  : C.C
# @File    : study2.py
import calendar

import datetime
import keyword

cal = calendar.month(2017,2)

print("输出2017年2月份的日历")

print(cal)


datetim = datetime.datetime.now()


print("当前年份为：%s" % datetim.year)


str = "我是"

str = "猪?^(*￣(oo)￣)^"

print(str)


#
# # 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print (arg1)
#     for var in vartuple:
#         print(var)
#     return;
#
#
#
# # 调用printinfo 函数
# printinfo(10);
# printinfo(80,70, 60, 50);


def goadd(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return goadd(x-1) + goadd(x-2) + goadd(x-3)


print("存在的可能数是：",goadd(5))
print("存在的可能数是：11111")
