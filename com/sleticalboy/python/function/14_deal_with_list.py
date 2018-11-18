#!/usr/bin/env python
# -*- coding=utf-8 -*-


# 使用函数处理列表
def handle_list(names):
    """遍历列表"""
    for name in names:
        print("Hello, " + name.title() + "!")


# 调用函数处理列表
user_names = ['lee bin', 'jack', 'tom']
# 创建列表副本, 禁止函数修改列表内容
# [除非必要，否则不要这么做，因为这样做会有额外的内存开销]
handle_list(user_names[:])


# 传递任意数量的形参，这类似于 java 中的可变参数, 同样的这个参数只能放在形参的最后一个位置
def make_pizzas(size=int(), *toppings):
    """概述要制作的 pizza """
    print('\nMaking a ' + str(size) + '-inch pizza with the flowing toppings:')
    for top in toppings:
        print('- ' + top)


make_pizzas(16, 'beef')
make_pizzas(15, 'beef', 'fruit', 'meat', 'fish')
