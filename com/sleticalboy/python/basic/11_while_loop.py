#! /usr/bin/env python
# -*- encoding=utf-8 -*-

num = 1
while num <= 8:
    print(num)
    num += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nor you can enter 'quit' to end the program. "
message = ""
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        print(False)
        break
    else:
        print(message)

responses = {}
active = True

while active:
    # key
    name = input("\nWhat's your name? ")
    # value
    response = input("Which mountain would you like to climb someday?")
    # 存储
    responses[name] = response
    # 提示是否重复
    repeat = input("Would you like to let another person respond? (yes/no)")
    # 满足条件则退出
    if repeat == 'no':
        active = False

print('----- over -----')
# 循环遍历结果
for name, response in responses.items():
    print(name + " would like climb " + response + ".")
