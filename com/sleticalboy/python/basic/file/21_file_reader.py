#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 读取文件内容

# 使用绝对路径
# path = '/home/sleticalboy/code/python/Pylearn/com/sleticalboy/' \
#        'python/file/pi_digits.txt'
# 使用相对路径
path = './pi_digits.txt'

# 读取一个文件的内容
print('读取文件的全部内容')
with open(path) as file_obj:
    # 读取文件的全部内容
    contents = file_obj.read()
    # 使用 rstrip() 去除最后一个空行
    print(contents.rstrip())
    # 关闭文件
    # file_obj.close()

# 圆周率后100万位
path = './pi_million_digits.txt'
print('逐行读取并使用文件内容')
pi = ''
with open(path) as file_obj:
    # 逐行读取
    for line in file_obj:
        # print(line.rstrip())
        # 去除字符串两端的空格
        pi += line.strip()

print("pi's length is " + str(len(pi)))
print(pi[:52])

# 你的生日是否在圆周率后的100万位中
birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi:
    print('Your birthday appears in the first million digits of pi!')
else:
    print("Your birthday doesn't appear in the first million digits or pi.")
