#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午4:29
# @Author  : C.C
# @File    : demo76.py

# 题目：编写一个函数，
# 输入n为偶数时，调用函数求1/2+1/4+...+1/n,
# 当输入n为奇数时，调用函数1/1+1/3+...+1/n


def double(number):
    data = []
    for i in range(2, number + 1, 2):
        data.append(1.0 / i)
    return data


def single(number):
    data = []
    for i in range(1, number + 1, 2):
        data.append(1.0 / i)
    return data


def totals(number, isType):
    if isType:
        num = double(number)
    else:
        num = single(number)

    return sum(num)


if __name__ == '__main__':
    number = int(input("请输入一个正整数:"))
    if number % 2 == 0:
        total = totals(number, True)
    else:
        total = totals(number, False)

    print("求得和是：", total)
