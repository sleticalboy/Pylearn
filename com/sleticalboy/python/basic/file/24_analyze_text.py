#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 收集错误日志的文件
log_path = "error.log"


# 收集日志
def collect_error_log(msg):
    """收集错误日志的文件"""
    try:
        with open(log_path, 'a') as error_log:
            error_log.write(msg + "\n")
    except FileNotFoundError:
        pass  # 不处理，不想让用户看到某些敏感信息


# 分析文本
def count_words(file_name):
    """分析文本"""
    mode = 'r'
    try:
        with open(file_name, mode) as file_obj:
            content = file_obj.read()
    except FileNotFoundError:
        log = "The file <" + file + "> was not found"
        collect_error_log(log)
    else:
        length = len(content.split())
        print("The file " + file_name + " has " + str(length) + " words")


file_names = ['alice.txt', 'siddhartha.txt', 'little_women.txt',
              'dict.txt']
for file in file_names:
    count_words(file)
