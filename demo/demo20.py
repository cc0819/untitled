#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午2:22
# @Author  : C.C
# @File    : demo20.py

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

def blance(num):
    height = []
    he = 100
    for i in range(1, num ):
        he /= 2
        height.append(he)

    return min(height)/2

print("反弹10次后的高度是：", blance(10))