#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 从一个模块导入多个类时，要用逗号分隔开
# from com.sleticalboy.python.oop.car import ElectricCar, Car, Battery
# 从一个模块中导入所有类
# from com.sleticalboy.python.oop.car import *
from com.sleticalboy.python.oop.car import ElectricCar

# 实例化对象
tesla = ElectricCar('tesla', 'model s', 2018)

print(tesla.get_descriptive_name())
# 调用子类特有的方法
tesla.describe_battery()
# 调用父类的方法
tesla.update_odometer(100)
tesla.read_odometer()
# 调用重写的父类方法
tesla.fill_gas_tank()

tesla.battery.dump_range()
