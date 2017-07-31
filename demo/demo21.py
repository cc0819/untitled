#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/31 下午2:22
# @Author  : C.C
# @File    : demo21.py

# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，
# 还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。


remain2 = 1
for day in range(0, 9):
    remain1 = (remain2 + 1) * 2
    remain2 = remain1


print("第一天共摘了：", remain1)