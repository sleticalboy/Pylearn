#!/usr/bin/env python
# -*- coding=utf-8 -*-

from collections import OrderedDict

like_languages = OrderedDict()

like_languages['jen'] = 'python'
like_languages['jack'] = 'java'
like_languages['tom'] = 'c++'
like_languages['mick'] = 'perl'
print(like_languages)

for name, lan in like_languages.items():
    print(name.title() + "'s favorite language is " + lan.title() + ".")
