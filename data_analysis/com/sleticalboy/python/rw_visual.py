#!/usr/bin/env python
# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt
from com.sleticalboy.python.random_walk import RandomWalk

# 不断地模拟随机漫步
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘制窗口的尺寸
    plt.figure(dpi=64, figsize=(10, 6))
    point_numbers = list(range(rw.num_point))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.cmapname, edgecolors='none', s=1)
    # 突出显示第一和最后一个点
    plt.scatter(0, 0, c='green', edgecolors='none', s=40)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=40)
    # 不支持中文，不知道为什么
    # plt.title('模拟随机漫步')
    # 隐藏坐标轴
    plt.Axes.get_xaxis(plt.axes()).set_visible(False)
    plt.Axes.get_yaxis(plt.axes()).set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
