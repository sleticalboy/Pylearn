#! /usr/bin/env python
# -*- encoding=utf-8 -*-

# 函数体与函数体或者调用函数的语句之间推荐空出两行空白


# 定义函数，并向函数传递参数
def greet_user(name):
    """打印语句"""  # 文档注释
    print('Hello ' + name.title())


# 一个函数可调用多次
greet_user('sleticalboy')
greet_user('lee bin')
# 关键字实参
greet_user(name='jack')


# 定义函数，描述一个宠物
def describe_pet(pet_name, pet_type='dog'):
    """显示宠物信息"""
    print("I have a " + pet_type + ".")
    print("My " + pet_type + "'s name is " + pet_name.title() + ".")


# 调用函数，当有默认值时，参数可以不用传递
describe_pet(pet_name='reek')
# 等效函数调用，实参指定时可以不需要确定顺序
describe_pet(pet_type='monkey', pet_name='wukong sun')
