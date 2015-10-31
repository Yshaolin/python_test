#!/usr/bin/env python3
#-- coding:utf-8 --

import os
import os.path, re, sys

L = []
def dir(top):
    if os.path.isdir(top):
        for x in os.listdir(top):
            for i in dir(os.path.join(top, x)):
                yield i
    elif os.path.isfile(top):
        yield top

#def new_match_file(patten):
#    def decoretor(func):
#        def wrapper(*args, **kw):
#            return func(patten, *args)
#        return wrapper
#    return decoretor


#@new_match_file('test.*')
def match_file(top, patt=''):
    def func(top, patten=patt):
        pat = re.compile(patten)
        if re.match(pat, os.path.split(top)[1]):
            L.append(top)
    return func

f = match_file('.', 'test.*')

x = dir('.')
for i in x:
    f(i)

print L
