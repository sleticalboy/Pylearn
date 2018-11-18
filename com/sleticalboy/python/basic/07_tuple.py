#! /usr/bin/env python
# -*- encoding=utf-8 -*-

# 元组一经定义，其内容不可修改，但是可以重新赋值

# 定义个元组
rectangle = (3, 4)
print(rectangle)
print(rectangle[0] + rectangle[1])

# 遍历元组
print('遍历元组')
for value in rectangle:
    print(value)

print("重新赋值")
rectangle = (7, 12)
print(rectangle)
