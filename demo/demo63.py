#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 上午10:06
# @Author  : C.C
# @File    : demo63.py

# 题目：画椭圆。　
from tkinter import *

if __name__ == '__main__':
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width=400, height=600, bg="red")
    canvas.pack()

    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5

    mainloop()
