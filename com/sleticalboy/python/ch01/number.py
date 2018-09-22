#!/usr/bin/env python
# -*- coding=utf-8 -*-

print('hello python')

num = 90

if True:
    print(num)
else:
    print('\tthis is not value')

var = 0
while var < 3:
    print(var)
    var = var + 1

# list 列表
# tuple 元组
# print(dict.__len__(abs(8))) 字典
# print(bool.bit_length(True)) bool

num = '123'

print(type(int(num, base=10)))
print(type(num))
print(int('07101', base=8))  # 进制转化 base=2/4/8/16
print(int('a', base=16))
print(int(num, base=10).bit_length())
print(int.bit_length(4))
