#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/1 上午12:00
# @Author  : C.C
# @File    : study1.py
import math
import random

num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)

x=2.1


print("choice随机数字："+str(random.choice(range(10))))
print("random随机数字："+str(random.random()*10))


list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200,200]
list1.extend(list2)
print ("list1 extend list2:",list1)

list2.sort()
print("list1 sort",list2)

tup1 = (50,12,18,39,89)
tup2 = (50,56,30)

print("tuple:",tup1)

