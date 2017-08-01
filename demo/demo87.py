#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午11:44
# @Author  : C.C
# @File    : demo87.py

# 题目：回答结果（结构体变量传递）。

if __name__ == '__main__':
    class Student:
        x = 0
        c = 0


    def f(stu):
        stu.x = 10
        stu.c = "haha"


    s = Student();
    s.x = 3
    s.c = "b"
    f(s)

    print(s.x)
    print(s.c)
