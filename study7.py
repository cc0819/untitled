#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/26 下午4:23
# @Author  : C.C
# @File    : study7.py 线程学习,线程同步
import threading

import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting",self.name)
        # 获取锁，成功获得后会返回True，可选参数timeout不填写的时候将会一直阻塞直到获得锁定，否则超时后会返回False
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()# 释放锁

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" %(threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []


# 创建线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()

print("Exiting Main Thread")




