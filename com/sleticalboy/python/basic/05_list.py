# !/usr/bin/env python
# -*- encoding=utf-8 -*-

# 列表
languages = ['python', 'java', 'c#', 'php']
print(languages)

# 查询列表的第一个元素
print('查询列表的第一个元素')
print(languages[0])

# 查询列表最后一个元素
print('查询列表最后一个元素')
print(languages[-1])

# 修改列表元素
print('修改列表元素')
languages[0] = 'perl'
print(languages)

# 向列表[末尾]添加元素
print('向列表[末尾]添加元素')
languages.append('python')
print(languages)

# 向列表指定位置插入元素
print('向列表指定位置插入元素')
languages.insert(0, 'c++')
print(languages)

# 临时排序列表
print('临时排序列表')
print(sorted(languages))
print(languages)

# 对列表永久排序
print('对列表永久排序')
languages.sort(reverse=True)
print(languages)

# 删除指定位置的元素
del languages[0]
print(languages)

# 弹出元素[不指定索引默认是最后一个]
print('弹出元素[不指定索引默认是最后一个]')
pop_element = languages.pop()
print('The last element in this list is ' + pop_element)
print(languages)

# 删除列表中的指定元素
print('删除列表中的指定元素')
languages.remove('perl')    # 返回值类型是 None
print(languages)

languages.insert(0, 'android')
languages.insert(-1, 'ios')

# 翻转列表
print('翻转列表')
languages.reverse()
print(languages)

# 计算列表长度
print('计算列表长度')
length = len(languages)
print(length)


