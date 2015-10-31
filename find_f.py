#!/usr/bin/env python3
#-- coding:utf-8 --

import os
import os.path, re, sys

L = []
def dir(top, patt, func):
    if os.path.isdir(top):
        for x in os.listdir(top):
            dir(os.path.join(top, x), patt, func)
    elif os.path.isfile(top):
        func(top, patt)

def match_file(file_name, patten):
    pat = re.compile(patten)
    if re.match(pat, os.path.split(file_name)[1]):
        return L.append(file_name)

print dir('.', '.*py', match_file)
