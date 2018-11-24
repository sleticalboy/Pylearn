#!/usr/bin/env python
# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt

# 绘制折线图

# 生成列表
values = list(range(1, 101))
squares = [value ** 2 for value in values]
# print(squares)
# 设置曲线粗细
plt.plot(values, squares, linewidth=2)

# 设置标题并给坐标轴加上标签以及字体大小
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置坐标轴单位长度
plt.tick_params(axis='both', labelsize=8)
# 显示
plt.show()
