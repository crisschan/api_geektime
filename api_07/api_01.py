#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __from__ = 'api_07'
# __author__ = 'CrissChan<criss.chan@foxmail.com >'
# __mtime__ = '2020/3/9 10:37 上午'
# __File__  = api_01.py
# __instruction__='ws的例子'

from common import Common
# 建立和WebSocket接口的链接
con = Common('ws://echo.websocket.org','ws')
# 获取返回结果
result = con.send('Hello, World...')
#打印日志
print(result)
#释放WebSocket的长连接
del con