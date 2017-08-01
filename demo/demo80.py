#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/1 下午6:01
# @Author  : C.C
# @File    : demo80.py

# 题目：海滩上有一堆桃子，五只猴子来分。
# 第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
# 第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？


def monkey(param):
    if param == 5:
        return 6
    else:
        return monkey(param + 1)




if __name__ == '__main__':
    print(monkey(5))
