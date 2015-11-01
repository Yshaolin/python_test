#!/usr/bin/env python3
#-- coding:utf-8 --

import os
import os.path
import re
import sys
from multiprocessing import Process

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
def match_file(top, patten=''):
    pat = re.compile(patten)
    if re.match(pat, os.path.split(top)[1]):
        print top

x = dir('/home/ubuntu-4118/Documents')
for i in x:
    p = Process(target=match_file, args=(i,'test.*'))
    p.start()
print L
