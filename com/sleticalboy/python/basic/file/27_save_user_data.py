#!/usr/bin/env python
# -*- coding=utf-8 -*-

import json

# 保存用户数据

filename = 'user_info.json'
mode = 'w'

try:
    # 尝试读取用户数据，如果不存在则执行 except 中的代码记录用户信息
    with open(filename) as user_file:
        username = json.load(user_file)
except FileNotFoundError:
    # 存储用户数据
    username = input("What's your name? ")
    try:
        with open(filename, mode) as user_file:
            json.dump(username, user_file)
            print("We'll remember you when you come back, " + username + "!")
    except FileNotFoundError:
        pass
else:
    print("Welcome back, " + username + "!")
