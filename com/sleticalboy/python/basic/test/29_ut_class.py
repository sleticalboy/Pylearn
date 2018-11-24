#!/usr/bin/env python
# -*- coding=utf-8 -*-
import unittest as ut

from com.sleticalboy.python.basic.test.survey import AnonymousSurvey


def run_language_survey():
    ques = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(ques)
    my_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input("Language: ")
        if response == 'q':
            break
        my_survey.save_response(response)
    print("\nThank you for the survey!")
    my_survey.show_response()


# run_language_survey()
class TestAnonymousSurvey(ut.TestCase):
    """测试 AnonymousSurvey"""

    # 测试类内部使用
    def setUp(self):
        ques = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(ques)
        self.responses = ['english', 'chinese', 'spanish']

    def test_save_single_response(self):
        """测试单个结果能否被保存"""
        # ques = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(ques)
        self.my_survey.save_response(self.responses[0])
        self.assertIn("english", self.my_survey.responses)

    def test_save_multi_response(self):
        """测试多个结果能否被保存"""
        # ques = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(ques)
        # my_survey.save_response("english")
        # my_survey.save_response("chinese")
        # my_survey.save_response("spanish")

        for resp in self.responses:
            self.my_survey.save_response(resp)

        for resp in self.responses:
            self.assertIn(resp, self.my_survey.responses)


ut.main()
