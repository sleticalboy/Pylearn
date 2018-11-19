#!/usr/bin/env python
# -*- coding=utf-8 -*-

import json

# json 模块读取文件数据

path = 'numbers.log'
mode = 'r'

try:
    with open(path, mode) as f_obj:
        contents = json.load(f_obj)
except FileNotFoundError:
    pass
else:
    print(contents)
