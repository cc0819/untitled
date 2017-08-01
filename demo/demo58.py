#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午11:29
# @Author  : C.C
# @File    : demo58.py

# 题目：画图，学用rectangle画方形。　
from tkinter import *

if __name__ == '__main__':

    root = Tk()
    root.title("Canvas")
    canvas = Canvas(root, width=400, height=400,bg = "yellow")
    canvas.pack()

    x0 = 200
    y0 = 200
    x1 = 300
    y1 = 300

    for i in range(16):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    mainloop()
        

