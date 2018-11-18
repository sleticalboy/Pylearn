#! /usr/bin/env python
# -*- encoding=utf-8 -*-

values = [element ** 2 for element in range(1, 11)]
print('循环中添加 if 控制语句')
for value in values:
    if value % 2 == 0:
        print('\t' + str(value) + ' is an even')
    else:
        print('\t\t' + str(value) + ' is an odd')

# 条件测试
print('条件测试')
car = 'benz'
print('benz' == car)
print('bmw' == car)
print('bmw' != car)
car = 'bmw'
print('BmW'.lower() == car)

# 比较数字
print('比较数字')
age = 24
print(24 == age and 44 >= age)
print(22 != age or 24 == age)
print(23 <= age)
print(29 >= age)

values = list(range(1, 11))
print(9 in values and 99 not in values)

for e in values:
    if e % 2 == 0:
        print("multiple of 2")
    elif e % 3 == 0:
        print('multiple of 3')
    else:
        print('known of ' + str(e))

print()

# bool 表达式
print('bool 表达式')
right = True
print(right)


