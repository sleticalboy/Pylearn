#!/usr/bin/env python
# -*- coding=utf-8 -*-
from random import choice


class RandomWalk:
    """生成随机漫步数据"""

    def __init__(self, num_point=5000):
        """初始化数据"""
        self.num_point = num_point
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """填充列表"""
        while len(self.x_values) < self.num_point:
            # x 方向
            # choice: 从给定的序列中随机选一个
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            # 范围： [-4, 4]
            x_step = x_direction * x_distance
            # y 方向
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
