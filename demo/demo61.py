#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午9:41
# @Author  : C.C
# @File    : demo61.py

# 打印出杨辉三角形（要求打印出10行如下图）。

def pascal(param):
    data = [[1]]
    for i in range(1, param):
        data.append([1])
        for j in range(1, i):
            data[i].append(data[i - 1][j - 1] + data[i - 1][j])
        data[i].append(1)

    return data


if __name__ == '__main__':
    pa = pascal(10)
    for r in pa:
        print(r)
