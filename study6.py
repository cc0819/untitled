#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/7/23 下午10:51
# @Author  : C.C
# @File    : study6.py
import chardet
import requests
import urllib3
import urllib.request


def oneMethod():
    # 抓取数据
    param = {"action": "", "start": "0", "limit": "1"}
    returndata = requests.get("https://movie.douban.com/j/chart/top_list?type=5&interval_id=50%3A40", data=param,
                              verify=False)
    print(returndata.text)


def twoMethod():
    # 抓取数据
    url = "http://www.missevan.com/"
    # url = "http://www.cnblogs.com/jtjds/p/5326200.html"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()\
        # .decode("utf-8")
    tempData = chardet.detect(data)
    response.close()
    print(tempData)


def threeMrthod():
    url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=50%3A40&action=&start=0&limit=1"
    request = urllib.request.Request(url)
    request.add_header("User-Agent","Mozilla/5.0")
    response = urllib.request.urlopen(request)
    data = response.read()
    response.close()
    print(data)



def main():
    # oneMethod() #基本方法
    twoMethod() #使用urllib抓取
    # threeMrthod() #构建request添加header抓取


if __name__ == '__main__':
    main()
