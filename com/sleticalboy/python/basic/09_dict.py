#! /usr/bin/env python
# -*- encoding=utf-8 -*-

# 字典， 类似 Java 中的 Map

student = {'name': 'Lee Bin', 'age': 23}
print(student)
print(student['name'])
print(student['age'])

# 添加一个键值对
print('添加一个键值对')
student['language'] = 'Python'
student['score'] = 99
print(student)

# 删除键值对
print('删除键值对')
del student['language']
print(student)

# 遍历字典
print('遍历字典')
student['language'] = 'Python'
for k, v in student.items():
    print('\t' + str(k) + ', ' + str(v))

# 遍历 key
print('遍历 keys')
for k in student.keys():
    print('\t' + str(k))

# 遍历 values
print('遍历 values')
for v in student.values():
    print('\t' + str(v))

# 字典嵌套列表
# 字典嵌套字典
# 列表嵌套列表
# 列表嵌套字典
