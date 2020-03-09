#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __from__ = 'api_geektime_example'
# __author__ = 'CrissChan<criss.chan@foxmail.com >'
# __mtime__ = '2020/3/3 6:04 下午'
# __File__  = 1.py
# __instruction__='04节第一个测试脚本代码段'


import requests

# 建立url_index的变量，存储战场的首页
url_index = 'http://127.0.0.1:12356/'
# 调用requests类的get方法，也就是HTTP的GET请求方式，访问了url_index存储的首页URL，返回结果存到了response_index中
response_index = requests.get(url_index)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容：' + response_index.text)
