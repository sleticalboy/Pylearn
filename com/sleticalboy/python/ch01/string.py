#!/usr/bin/env python
# -*- coding=utf-8 -*-

name = "Home sweet home = ? & *"
print(name.__len__())  # 长度
print(name.endswith("e"))  # 结尾
print(name.startswith('h'))  # 开头
print(name.__contains__('m'))  # 包含
print('m' in name)  # 判断
print(name.title())  # 首字母转大写

print(name.upper())  # 转大小写
print(name.casefold())  # 增强小写
print(name.lower())  # 小写
print(name.center(100, '-'))  # 宽度 长度 填充
print(name.count('e'))  # 计算子序列出现的次数

# print(name.encode())
# 查找
print(name.find('e'))

# 格式化
foo = 'hello {name}'
print(foo)
print(foo.format(name='alex'))
print(foo.format_map({'name': 'tony'}))

foo = 'my name is {0} and {1} years old'
print(foo)
print(foo.format('alex', 19))

# 字母数字判断
print("asd23".isalnum())
# 纯字母
print("asd".isalpha())
# 数字判断
print("123二三⑤陆九十九".isnumeric())
print("123".isdecimal())
print("123".isdigit())
# 数字, 字母下划线[标识符]
print("_12ju3_".isidentifier())
print("i_i9d+ii_0i".islower())
print("123412\\t34")
print("123412\t34".isprintable())
print(" d".isspace())
print(" " in " d")
print(" d".__contains__(" "))
# 判断首字母是否大写
print(str.istitle("Tss sss"))
# 首字母转换成大写
print(str.title('Return True if S is a titlecased string and there is at least one'))
# 拼接
print(str.join('_', '132'))
# 左右填充
print(str.ljust("123", 10, "-"))
print(str.rjust("123", 10, "-"))
# n 个一组进行补充
tabs = 'asdfasasdfas\tasdfasasdfas\tasdfasasdfas\tasdfasasdfas\tasdfasasdfas'
print(tabs.expandtabs(20))
# replace
print(str.replace("hello world", "l", ''))
# equals
print(str.__eq__('123', '123'))
# split
print(str.split('123', ','))
print(str.split('123,456,789', ','))
# enhance trim
print(str.strip('123 \t\r\n'))
print(str.strip('4441234', '4'))
print(str.replace('4441234', '4', ''))
print(str.split(tabs, '\t'))
print(str.splitlines('asdf\nasd\n', False))
# 大小写转换
print(str.swapcase('EjISkosU'))
# 索引
print(str.index('1234', '4'))
print('1234'[0:-1])
print(len('-----'))
