#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 写入文件

file_name = 'simple_msg.txt'
mode = 'a'

# w: write 会覆盖文件之前的内容
# a: append 不会覆盖，会追加到文件末尾
# r: 只读模式
with open(file_name, mode) as file_obj:
    # 换行
    file_obj.write('hello python.\n')
    file_obj.write('I love Python.\n')
