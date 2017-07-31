#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午2:23
# @Author  : C.C
# @File    : demo22.py

# 两个乒乓球队进行比赛，各出三人。
# 甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

m = ["a", "b", "c"]
n = ["x", "y", "z"]
index = []

for i in range(3):
    if m[i] != 'a' and m[i] != 'c':
        index.insert(i, 'x')
    elif m[i] != 'c':
        index.insert(i, 'z')
    else:
        index.insert(i, 'y')

print("比赛的分组为:")
print("一队为：", m)
print("二队为：", index)