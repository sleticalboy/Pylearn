#!/usr/bin/env python
# -*- coding=utf-8 -*-


class Dog:
    """创建 Dog 类"""

    def __init__(self, name, age):
        """初始化一些属性"""
        self.name = name
        self.age = age

    def sit(self) -> None:  # 指定函数的返回值类型
        """sit 方法"""
        print(self.name.title() + " is now sitting.")

    def roll_ever(self) -> None:
        """ roll_over 方法"""
        print(self.name.title() + " rolled over!")

    def to_string(self) -> None:
        """输出自身的一些属性"""
        print("the dog name is " + self.name.title() + " and " + str(self.age)
              + " years old.")
