#!/usr/bin/env python
# -*- coding=utf-8 -*-


def make_pizza(size=int(), *toppings):
    """概述要制作的 pizza """
    print('\nMaking a ' + str(size) + '-inch pizza with the flowing toppings:')
    for top in toppings:
        print('- ' + top)


def dump(msg):
    """打印传递过来的内容"""
    print(msg)
