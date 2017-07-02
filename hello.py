#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

x = "a"
y = "b"
name = "啊哈蛤呢"
a = b = c = 1

d, e, f = 2, 5, "haha"

print("hello word,", end='')
print("你好世界")

print(name)  # 注释

print(name + "哈哈哈哈")

print(name[1:3])

for letter in "Python":
    print("当前字母是+" + letter)

rows = int(input("请输入列数："))
i = j = k = 1  # 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
# 等腰直角三角形1
print("等腰直角三角形1")
for i in range(0, rows):
    for k in range(0, rows - i):
        print(" * ", end="")
        k += 1
    i += 1
    print("\n")

# #打印实心等边三角形
# print ("打印空心等边三角形，这里去掉if-else条件判断就是实心的")
# for i in  range(0,rows+1):
#     for j in range(0,rows-i):
#         print(" ",end="")
#         j+=1



# 打印菱形
print("打印等边菱形，这里去掉if-else条件判断就是实心的")
for i in range(rows):  # 上半部分
    for j in range(rows - i):  # 输出空格
        print(" ", end="")
        j += 1
    for k in range(rows-j+1):#输出*
        print("* ", end="")
        k += 1
    print("\n")
    i += 1


for i in  range(rows-1):#下半部分
    for j in range (i+1):
        print(" ",end="")
        j+=1
    for  k in range(rows-i-1):
        print(" *",end="")
        k+=1
    print("\n")
    i+=1





if True:
    print("True")
else:
    print("false")

while True:
    s = int(random.randint(1, 3))
    if s == 1:
        end = "石头"
    elif s == 2:
        end = "剪子"
    elif s == 3:
        end = "布"

    m = input('输入 石头、剪子、布,输入"end"结束游戏:')
    list = ['石头', "剪子", "布"]

    if (m not in list) and (m != "end"):
        print("输入错误，请重新输入！")
    elif m == "end":
        print("退出游戏...")
        break
    elif m == end:
        print("电脑出了" + end + "平局")
    elif (m == '石头' and end == '剪子') or (m == '剪子' and end == '布') or (m == '布' and end == '石头'):
        print("电脑出了： " + end + "，你赢了！")
    elif (m == '石头' and end == '布') or (m == '剪子' and end == '石头') or (m == '布' and end == '剪子'):
        print("电脑出了： " + end + "，你输了！")
