#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 捕获异常并处理

# ZeroDivisionError
try:
    print(5 / 0)
except ZeroDivisionError:
    print('You can not divide by zero')

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first = input("\nFirst number: ")
    if first == 'q':
        break
    second = input('\nSecond number: ')
    if second == 'q':
        break
    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print('You can not divide by zero')
    else:
        print("The answer is " + str(answer))

# FileNotFoundError

path = 'hello.txt'
try:
    with open(path, 'r') as file_obj:
        content = file_obj.read()
except FileNotFoundError:
    print("The file " + path + " was not found")
else:
    print(content)
