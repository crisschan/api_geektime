#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __from__ = 'api_geektime_example'
# __author__ = 'CrissChan<criss.chan@foxmail.com >'
# __mtime__ = '2020/3/3 6:06 下午'
# __File__  = 2.py
# __instruction__='04节第二个测试脚本代码段'

import requests

# 建立url_login的变量，存储战场系统的登录URL
url_login = 'http://127.0.0.1:12356/login'
# username变量存储用户名参数
username = 'criss'
# password变量存储密码参数
password = 'criss'
# 拼凑body的参数
payload = 'username=' + username + '&password=' + password
# 调用requests类的post方法，也就是HTTP的POST请求方式，
# 访问了url_login，其中通过将payload赋值给data完成body传参
response_login = requests.post(url_login, data=payload)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容：' + response_login.text)
