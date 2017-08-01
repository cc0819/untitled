#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午10:38
# @Author  : C.C
# @File    : demo56.py

# 题目：画图，学用circle画圆形。
from tkinter import *

if __name__ == '__main__':

    canvas = Canvas(width = 600, height = 300, bg = "yellow")
    canvas.pack(expand = YES, fill = BOTH)
    a, b = 1, 1

    for i in range(1,21):
        canvas.create_oval(310 - a,250 - a,310 + a,250 + a, width=1)
        a += b
        b += 0.5

    mainloop()

