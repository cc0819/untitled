#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/30 下午11:08
# @Author  : C.C
# @File    : demo15.py

# 利用条件运算符的嵌套来完成此题：
# 学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示，
# 60分以下的用C表示

score = int(input("请输入考试的分数："))

if score >= 90:
    show = "A"
elif score >= 60:
    show = "B"
else:
    show = "C"

print("%d的考试分数评级是%s" %(score, show))
