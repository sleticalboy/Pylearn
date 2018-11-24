#!/usr/bin/env python
# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt

# 准备数据
values = list(range(1, 1001))
squares = [value ** 2 for value in values]
# 绘制散点图
# c: color 字符串或者 rgb
# s: size
# edgecolors: 轮廓的颜色
# plt.scatter(values, squares, c='blue', edgecolors='none', s=1)
# 使用颜色映射(每次运行程序生成图片中的曲线颜色都是不同的)
plt.scatter(values, squares, c=squares, cmap=plt.cm.cmapname,
            edgecolors='none', s=1)
# 标题
plt.title('Square Numbers', fontsize=14)
# 坐标轴
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
# 设置坐标轴的取值范围 x: 0~[1000 + 100], y: 0~[1000 ** 2 + 100 ** 2]
plt.axis([0, values[-1] + 100, 0, squares[-1] + 100 ** 2])
# 显示
# plt.show()
# 自动保存图片
plt.savefig('squares_plot.png', bbox_inches='tight')
