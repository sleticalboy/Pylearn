#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Python 中的单元测试

import unittest as ut


def get_format_name(first, last, middle=''):
    """获取格式化之后的名字"""
    full_name = first.title() + " "
    if middle:
        full_name = full_name + middle.title() + " " + last.title()
    else:
        full_name = full_name + last.title()
    return full_name


class NameTestCase(ut.TestCase):
    """测试 get_format_name() 函数"""

    def test_first_last_name(self):
        format_name = get_format_name(first="lee", last="bin")
        # 可以通过的测试
        # 断言 equal
        self.assertEqual(format_name, "Lee Bin")

    def test_first_middle_last_name(self):
        format_name = get_format_name("lee", "bin", "little")
        # 不能通过的测试
        self.assertEqual(format_name, "Le Little Bin")


# 执行测试
ut.main()
