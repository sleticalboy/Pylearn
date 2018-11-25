#!/usr/bin/env python
# -*- coding=utf-8 -*-
from random import randint


class Die:
    """模拟掷骰子"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)
