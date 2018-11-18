#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 一个模块中可以存储多个类


class Car:
    """ Car 类"""

    def __init__(self, make, model, year):
        """ init """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) -> str:
        """返回详细信息"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc

    def increment_odometer(self, miles):
        """
        增加 odometer, 禁止回调
        """
        if miles > 0:
            self.odometer_reading += miles
        else:
            print('you cannot roll back the odometer!')

    def update_odometer(self, odometer):
        """
        更新 odometer, 禁止回调
        """
        if odometer > self.odometer_reading:
            self.odometer_reading = odometer
        else:
            print('you cannot roll back the odometer!')

    def read_odometer(self):
        """输出里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def fill_gas_tank(self):
        """加油"""
        print('you just fill the gas tank.')


# 继承自 Car 类
class ElectricCar(Car):
    """继承实现电动汽车"""

    def __init__(self, make, model, year):
        """
        首先需要初始化父类的属性
        接着初始化子类特有的属性: 电量
        """
        super().__init__(make, model, year)
        # 将 Battery 类用作属性
        self.battery = Battery()

    # 子类独有的方法
    def describe_battery(self):
        """输出电量信息"""
        print("This car has a " + self.battery.to_string() + "-kwh battery.")

    # 重写父类方法
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank.")


class Battery:
    """电池"""

    def __init__(self, size=70):
        self.size = size

    def dump_range(self) -> None:
        """打印续航能力"""
        remaining_range = 0
        if self.size == 70:
            remaining_range = 240
        elif self.size == 85:
            remaining_range = 270
        msg = "This car can go approximately " + str(remaining_range) \
              + " miles on a full charge"
        print(msg)

    def to_string(self) -> str:
        return str(self.size)
