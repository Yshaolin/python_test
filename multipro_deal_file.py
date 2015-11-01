#!/usr/bin/env python3
#-- coding:utf-8 --

import os
import os.path
import re
import sys
import struct
from multiprocessing import Process, Pool

#遍历指定目录，返回一个Iterator
def dir(top):
    if os.path.isdir(top):
        for x in os.listdir(top):
            for i in dir(os.path.join(top, x)):
                yield i
    elif os.path.isfile(top):
        yield top

#匹配指定文件，并启动子进程处理该文件
def match_file(top, patten=''):
    pat = re.compile(patten)
    if re.match(pat, os.path.split(top)[1]):
        p = Process(target=get_result, args=(top,))
        p.start()


#打开文件读取数据，并调用函数保存
def get_result(file_name):
    with open(file_name, 'rb') as rf:
        data = rf.read()
        nums = struct.unpack('f'*101, data)
        save_result(nums)

#保存数据到指定文件
def save_result(nums):
    with open('multipro_out.txt', 'a') as af:
        af.write(str(nums)+'\n')

#主体部分，指定目录，指定目标文件
if __name__ == '__main__':
    x = dir('/HOME/whu_bio_wtma_1/WORKSPACE/15_10_8/work')
    for i in x:
        match_file(i,'pol-a-[34].dat')
