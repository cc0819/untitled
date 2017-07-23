#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/10 上午10:14
# @Author  : C.C
# @File    : study3.py


class Students:
    stuCount = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Students.stuCount += 1

    def __del__(self):
        print("被销毁了")

    def __str__(self):
        return  'Student (%s, %d)' % (self.name, self.age)


    def __add__(self, other):
        return Students(self.name + other.name, self.age + other.age)

    def displayCount(self):
        print("Total Students %d" % Students.stuCount)


    def displayStudent(self):
        print("Name : ", self.name,  ", Age: ", self.age)


stu1 = Students("小二",20)
stu2 = Students("张三",19)


stu1.displayStudent()
stu2.displayStudent()

print("Total students %d" % Students.stuCount)

setattr(stu1,"sex","female")
print("student sex ", hasattr(stu1,"sex"))

print(stu1+stu2)


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (counter._JustCounter__secretCount)  # 报错，实例不能访问私有变量