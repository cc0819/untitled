#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午3:49
# @Author  : C.C
# @File    : demo83.py

# 题目：求0—7所能组成的奇数个数。

if __name__ == '__main__':

    total = []
    s = 0
    for i in range(1, 9):
        if i == 1:
            s = 4
        elif i == 2:
            s *= 7
        else:
            s *= 8

        # total += s
        total.append(s)
        print(s)


    print("共可以组成 %d 个奇数" % sum(total))
