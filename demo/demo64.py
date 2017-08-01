#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午9:43
# @Author  : C.C
# @File    : demo64.py

# 题目：利用ellipse 和 rectangle 画图。。
from tkinter import *

if __name__ == '__main__':
    canvas = Canvas(width=400, height=600, bg="green")
    canvas.pack()

    left = 20
    right = 50
    top = 50
    num = 15

    for i in range(num):
        canvas.create_rectangle(20 - 2 * i, 20 - 2 * i, 10 * (2 + i), 10 * (2 + i))
        canvas.create_oval(250 - right, 250 - left, 250 + right, 250 + left)
        canvas.create_oval(250 - 20, 250 - top, 250-top, 250 + top)

        left += 5
        right += 5
        top += 10

mainloop()
