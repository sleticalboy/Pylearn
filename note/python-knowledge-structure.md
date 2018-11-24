# Python 知识结构

## Zen of Python: Python 之禅
- The Zen of Python, by Tim Peters
    - Beautiful is better than ugly.
    - Explicit is better than implicit.
    - Simple is better than complex.
    - Complex is better than complicated.
    - Flat is better than nested.
    - Sparse is better than dense.
    - Readability counts.
    - Special cases aren't special enough to break the rules.
    - Although practicality beats purity.
    - Errors should never pass silently.
    - Unless explicitly silenced.
    - In the face of ambiguity, refuse the temptation to guess.
    - There should be one-- and preferably only one --obvious way to do it.
    - Although that way may not be obvious at first unless you're Dutch.
    - Now is better than never.
    - Although never is often better than *right* now.
    - If the implementation is hard to explain, it's a bad idea.
    - If the implementation is easy to explain, it may be a good idea.
    - Namespaces are one honking great idea -- let's do more of those!

## basic: 基础
- hello python
- Python 中的变量
- Python 中的字符串
    - str()
    - lstrip()
    - rstrip()
    - strip()
    - split()
    - in 判断
- Python 中的数字
    - +, -, *, /, **(乘方)
    - int() 函数
- Python 中的列表[list]
    - append()
    - insert()
    - pop()
    - del 删除元素
    - remove() 
    - 列表切片
    - 列表拷贝
    - 遍历列表
        - for 循环
        - while 循环
- Python 中的元组[tuple]
    - 元组一经定义，内容不可变，但是可以重新赋值
- if 语句
- Python 中的字典[dict]
    - 类似 Java 中的 Map 集合，用于存储 k-v 映射的一种数据结构
    - 类似 json 语法
- 用户输入[input()]
    - 接收用户输入，用于在 terminal 中和用户进行交互

## function: 函数
- def 关键字定义函数
- 简单函数示例
- 传递任意数量的实参(类似Java中的可变参数)
- 函数返回值
- 函数等效调用
    - 实参指定时可以不需要确定顺序
- 使用函数处理列表/字典

## OOP: 面向对象编程
- class 关键字定义类
    - 类属性
    - 构造方法
    - 类方法
- 类的实例化
- 类的继承
    - 重写父类方法
    - 编写子类特有的方法

## file: 文件操作
- 打开文件
- 读取文件内容
    - 读取全部内容
    - 逐行读取
- 写入文件
- 异常处理
    - try except 语句
    - try except else 语句

## unittest: 单元测试
- assert[断言]
    - assertEqual()
    - assertNotEqual()
    - assertIn()
    - assertNotIn()
- TestCase[测试用例]
    - setUp()
    - test_***