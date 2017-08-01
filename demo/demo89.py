#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午5:47
# @Author  : C.C
# @File    : demo89.py

# 题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，
# 再将第一位和第四位交换，第二位和第三位交换。

if __name__ == '__main__':
    number = str(input("请输入一个四位数："))
    data = []
    for i in range(len(number)):
        temp = (int(number[i]) +5 ) % 10
        data.append(temp)

    data[0], data[3] = data[3], data[0]
    data[1], data[2] = data[2], data[1]

    print(data[0]*1000+data[1]*100+data[2]*10+data[3])
