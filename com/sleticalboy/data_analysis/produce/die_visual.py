#!/usr/bin/env python
# -*- coding=utf-8 -*-
import pygal
from com.sleticalboy.data_analysis.produce.die import Die

# 两个面书不同的骰子
die_1 = Die()
die_2 = Die(10)
result = []
times = 50000
# 投掷 times 次骰子并记录结果
for roll_num in range(times):
    result.append(die_1.roll() + die_2.roll())
# print(result)

frequencies = []
# 统计每个点数出现的次数并存储到列表中
min_result = 2
max_result = die_1.sides + die_2.sides + 1
for value in range(min_result, max_result):
    frequencies.append(result.count(value))
# print(frequencies)

# 将统计结果绘制到直方图中
hist = pygal.Bar()
hist._title = 'Result of rolling two D6 ' + str(times) + ' times.'
hist.x_labels = [str(value) for value in range(min_result, max_result)]
hist._x_title = 'Result'
hist._y_title = 'Frequency of Result'
hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
# 需要安装 cairosvg 依赖
# hist.render_to_png('die_visual.png')

# 用随机漫步呈现结果
# 要求 x 和 y 的值长度必须一致
# plt.scatter(frequencies, result, edgecolors='none', s=2)
# plt.show()
