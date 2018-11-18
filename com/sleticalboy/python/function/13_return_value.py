#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 函数返回值


def get_formatted_name(first_name, last_name, mid_name=''):
    """返回格式化的姓名"""
    full_name = first_name + " "
    if mid_name:
        full_name += mid_name + " "
    full_name += last_name
    return full_name.title()


# 调用函数
print(get_formatted_name('lee', 'bin', mid_name='big'))


# build a person
def build_person(first_name, last_name, age=int()):
    """构造 person 字典"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# 调用函数
print(build_person('lee', 'bin', age=25))
