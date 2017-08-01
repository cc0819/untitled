#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午4:47
# @Author  : C.C
# @File    : demo81.py

# 题目：809*??=800*??+9*??+1
# 其中??代表的两位数,8*??的结果为两位数，9*??的结果为3位数。
# 求??代表的两位数，及809*??后的结果。
import random

if __name__ == '__main__':
    secret = random.randint(1, 11)
    guess = int(input("请输入一个正整数:"))

    while guess != secret:
        guess = int(input("请再输入一个正整数:"))
        if guess == secret:
            break

    print("恭喜你猜对了")

    a = 809
    for i in range(10, 100):
        b = i * a + 1
        if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
            print(b, '/', i, ' = 809 * ', i, ' + ', b % i)
