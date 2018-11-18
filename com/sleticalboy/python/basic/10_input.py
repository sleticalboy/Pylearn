#! /usr/bin/env python
# -*- encoding=utf-8 -*-

message = input('Please enter your name: ')
greeter = 'Hello, ' + message.title() + '.'
print(greeter)

message = input("How old are you? ")
age = int(message)
message = "I'm " + str(age) + " years old."
print(message)

if age >= 18:
    print("Your're old enough to drive a car!")
else:
    print("Sorry, you're too young to drive a car.")
