#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __from__ = 'api_geektime_example'
# __author__ = 'CrissChan<criss.chan@foxmail.com >'
# __mtime__ = '2020/3/3 6:16 下午'
# __File__  = 4.py
# __instruction__='04第四个测试脚本测试脚本代码段'
from common import Common

# 登录页路由
uri = '/login'
# username变量存储用户名参数
username = 'criss'
# password变量存储密码参数
password = 'criss'
# 拼凑body的参数
payload = 'username=' + username + '&password=' + password
comm = Common()
response_login = comm.post(uri, params=payload)
print('Response内容：' + response_login.text)
