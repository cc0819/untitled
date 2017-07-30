#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/30 下午10:56
# @Author  : C.C
# @File    : demo13.py

# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。


vessel = []

for num in range(100, 1000):
    i = num // 100
    j = num // 10 % 10
    k = num % 10
    if num == i ** 3 + j ** 3 + k ** 3:
        vessel.append(num)


print("水仙花数有：", vessel)
