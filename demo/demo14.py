#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/30 下午11:07
# @Author  : C.C
# @File    : demo14.py

# 将一个正整数分解质因数。
# 例如：输入90,打印出90=2*3*3*5。

num = int(input("请输入要分解的大于1的正整数："))
if num <= 1:
    num = int(input("请输入正确的的大于1的正整数："))


defaul = num
leng = []
while num != 1:
    for i in range(2, num + 1):
        if num % i == 0:
            leng.append(i)
            num = num // i
            break

if leng[0] == defaul:
    leng.append(1)


print("分解的质因数是： %s" % leng)