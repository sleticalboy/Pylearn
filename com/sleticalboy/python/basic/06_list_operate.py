#! /usr/bin/env python
# -*- encoding=utf-8 -*-

languages = ['python', 'java', 'c#', 'php', 'go', 'perl']

# 循环遍历列表元素
for item in languages:
    print(item.title() + ', a well-known language.')
    print("\tI can't wait to learn it.")
print('There are all language I know.')

for value in range(1, 11):
    print(value)

# 使用 range 函数初始化列表
print('使用 range 函数初始化列表')
ages = list(range(18, 31, 2))
print(ages)

squares = []
for value in range(1, 11):
    # value = value ** 2
    squares.append(value ** 2)
print(squares)

# 求最小值
print('最小值')
print(min(squares))

# 求最大值
print('最大值')
print(max(squares))

# 求和
print('求和')
print(sum(squares))

# 列表解析
print('列表解析')
squares = [value ** 3 for value in range(1, 31, 2)]
print(squares)

# 切片
print('切片-前三个')
print(squares[:3])
print('切片-后三个')
print(squares[-3:])
print('遍历切片')
for value in squares[-5:]:
    print('\t' + str(value))
# 列表复制
print('列表复制')
my_squares = squares[:]
print(my_squares)
