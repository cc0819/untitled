#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午10:26
# @Author  : C.C
# @File    : demo69.py

# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
# 凡报到3的人退出圈子，问最后留下的是原来第几号的那位

if __name__ == '__main__':
    number = int(input("请输入围成圈的人数："))
    num = []
    for i in range(number):
        num.append(i + 1)

    index = 0
    while True:
        t = 0
        for i in range(1, len(num) + 1):
            index += 1
            print("---",index)
            if index % 3 == 0:
                num.pop(i - 1 - t)
                t += 1

        if len(num) == 1:
            print("最后留下的是第 %d 位数" % num[0])
            break
