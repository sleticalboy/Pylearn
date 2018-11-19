#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 导入 json 模块
import json

# 将数据写入文件中

numbers = [value ** 2 for value in range(1, 101)]

path = 'numbers.log'
mode = 'w'
try:
    with open(path, mode) as file_obj:
        json.dump(numbers, file_obj)
except FileNotFoundError:
    pass
