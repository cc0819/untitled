#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午1:04
# @Author  : C.C
# @File    : demo18.py

# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

a = int(input("a = "))
n = int(input("n = "))
num = 0
total = []
for index in range(n):
    num += a
    a *= 10
    total.append(num)


print("输出的数据为：", total)
print("计算总和为：", sum(total))
