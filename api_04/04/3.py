#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __from__ = 'api_geektime_example'
# __author__ = 'CrissChan<criss.chan@foxmail.com >'
# __mtime__ = '2020/3/3 6:09 下午'
# __File__  = 3.py
# __instruction__='04节第3个测试脚本代码段'

#
from common import Common
# 首页的路由
uri = '/'
# 实例化自己的Common
comm = Common()
# 调用你自己在Common封装的get方法 ，返回结果存到了response_index中
response_index = comm.get(uri)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容：' + response_index.text)
