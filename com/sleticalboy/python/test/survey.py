#!/usr/bin/env python
# -*- coding=utf-8 -*-


# 测试一个类
class AnonymousSurvey:
    """匿名调查问卷"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def show_response(self):
        if len(self.responses) != 0:
            print("Survey results:")
            for resp in self.responses:
                print("- " + resp.title())

    def save_response(self, new_resp):
        self.responses.append(new_resp)
