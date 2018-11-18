# !/usr/bin/env python
# -*- encoding=utf-8 -*-

name = 'lee bin'
print(name.title())

element = ' this is a left space, but i strip it'
# 去除左空格
print(element.lstrip())
element = 'this ia a right space, and i also strip it '
# 去除右空格
print(element.rstrip())
element = ' this is a left and right space, and ia strip them both'
# 去除两端的空格
print(element.strip())

# 切割成列表
print(element.split())

element = element.strip()

# 单词首字母大写
print(element.title())

# 全部转换成大写字母
element = element.upper()
print(element)

# 全部转换成小写字母
element = element.lower()
print(element)

f_name = 'bin'
l_name = 'lee'

# 字符串拼接/合并
full_name = l_name.title() + ' ' + f_name.title()
print(full_name)

# 制表符
tab = "Python\tC#\tJava"
print(tab)

# 换行符
line_feed = 'Python\nc#\nJava'
print(line_feed)
