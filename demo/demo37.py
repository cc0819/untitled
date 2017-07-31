#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午7:45
# @Author  : C.C
# @File    : demo37.py

# 对10个数进行排序。

# 冒泡排序
if __name__ == '__main__':
    number = [3,1,60,24,21,27,30,50,78,11]

    for i in range(0,len(number)):
        for j in range(i + 1,len(number)):
            if number[i] > number[j]:
                number[i], number[j] = number[j], number[i]

    print("排序后为%s" %number)