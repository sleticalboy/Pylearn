#!/usr/bin/env python
# -*- coding=utf-8 -*-
import json
import pygal
import math
from itertools import groupby

f_name = '../res/btc_close_2017.json'
s_file_name = '../res/close_line_chart.svg'
with open(f_name) as f_obj:
    data = json.load(f_obj)
    dates = []
    months = []
    weeks = []
    weekdays = []
    closes = []
    for item in data:
        date = item['date']
        month = int(item['month'])
        week = int(item['week'])
        weekday = item['weekday']
        close = int(float(item['close']))
        print('{} is month {} week {}, {}, the close price is {} RMB'
              .format(date, month, week, weekday, close))
        dates.append(date)
        months.append(month)
        weeks.append(week)
        weekdays.append(weekday)
        closes.append(close)
    line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
    line_chart._title = '收盘价'
    line_chart.x_labels = dates
    N = 20  # x 轴每隔 20 天显示一次
    line_chart._x_labels_major = dates[::N]
    # 数学处理函数
    closes_log = [math.log10(_) for _ in closes]
    line_chart.add('收盘价', closes_log)
    line_chart.render_to_file(s_file_name)


def draw_line(x_data, y_data, title, y_legend):
    """绘线"""
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line = pygal.Line()
    line._title = title
    line.x_labels = x_unique
    line.add(y_legend, y_mean)
    line.render_to_file(title + '.svg')
    return line


idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], closes[:idx_month], '收盘价月日均值(￥)', '月日均值')
line_chart_month

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week], '收盘价周日均值(￥)', '周日均值')
line_chart_week
