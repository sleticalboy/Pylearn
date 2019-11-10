#!/usr/bin/env python
# -*- coding=utf-8 -*-
import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

# f_name = '../res/sitka_weather_07-2014.csv'
# f_name = '../res/sitka_weather_2014.csv'
f_name = '../res/death_valley_2014.csv'
try:
    with open(f_name) as f_obj:
        reader = csv.reader(f_obj)  # 返回 reader 对象
        header_row = next(reader)   # 读取文件的第一行
        # print(header_row)
        # for index, column_header in enumerate(header_row):
        #     print(index, column_header)
        dates = []  # 日期
        highs = []  # 最高温
        lows = []   # 最低温
        for row in reader:
            try:
                cur_date = dt.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(cur_date, 'missing data')
            else:
                dates.append(cur_date)
                highs.append(high)
                lows.append(low)
        # print(dates, len(dates))
        # print(highs, len(highs))
        # print(lows, len(lows))

        # 绘制图表
        fig = plt.figure(dpi=64, figsize=(10, 6))
        # plt.plot(highs, c='red')
        plt.plot(dates, highs, c='red', alpha=0.5)
        plt.plot(dates, lows, c='blue', alpha=0.5)
        plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)   # 着色
        # 设置图形格式
        plt.title("Daily high and low temperatures - 2014\nDeath valley, CA")
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("T (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
except FileNotFoundError:
    print(f_name + ' not found')
