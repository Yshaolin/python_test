#!/usr/bin/env python3
#-- coding:utf-8 --

import os
import os.path, re, sys

L = []
def dir(top, func):
    if os.path.isdir(top):
        for x in os.listdir(top):
            dir(os.path.join(top, x), func)
    elif os.path.isfile(top):
        func(top)

def new_match_file(patten):
    def decoretor(func):
        def wrapper(*args, **kw):
            return func(patten, *args)
        return wrapper
    return decoretor


@new_match_file('test.*')
def match_file(*args):
    pat = re.compile(args[0])
    if re.match(pat, os.path.split(args[1])[1]):
        return L.append(args[1])



dir('.', match_file)
print L
