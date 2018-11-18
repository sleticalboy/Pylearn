#!/usr/bin/env python
# -*- coding=utf-8 -*-

from com.sleticalboy.python.oop.car import Car

# 实例化对象
audi = Car('audi', 'a4', 2016)
# 调用对象方法
audi.increment_odometer(23)
print(audi.get_descriptive_name())
audi.read_odometer()
audi.increment_odometer(233)
audi.read_odometer()
audi.fill_gas_tank()
