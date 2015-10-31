#!/usr/bin/env python3
#-- coding:utf-8 --

import os
import os.path, re, sys

args = len(sys.argv)
if args == 1:
    print ("Please input the absolute path you want to search:")
    dir_path = input()
    print ("Please input the file name you want to find:")
    file_name = input()
elif args == 2:
    print ("Please input the file name you want to find:")
    file_name = input()
elif len(sys.argv) == 3:
    dir_path = argv[1]
    file_name = argv[2]
else:
    sys.exit("Too many paraments!")

L = []
def find_file(fi, name):
    if os.path.isdir(fi):
        for x in os.listdir(fi):
            find_file(os.path.join(fi, x), name)
    elif os.path.isfile(fi):
            patt = re.compile(str(name))
            if re.search(patt, os.path.split(fi)[1]):
                L.append(fi)
    else:
        pass

if os.path.isdir(dir_path):
    find_file(dir_path, file_name)
else:
    sys.exit("The direc path is Illege!")
print (L)
