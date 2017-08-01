#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午10:51
# @Author  : C.C
# @File    : demo57.py

# 题目：画图，学用line画直线。
from tkinter import *

if __name__ == '__main__':

    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)

    x0 = 150
    y0 = 150
    x1 = 200
    y1 = 200
    
    for i in range(15):
        canvas.create_line(x0,y0,x0,y1, width=1, fill='red')
        x0 -=  5
        y0 -=  5
        x1 +=  5
        y1 +=  5

    x0 = 180
    y1 = 180
    y0 = 130
    for i in range(10):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='yellow')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()
