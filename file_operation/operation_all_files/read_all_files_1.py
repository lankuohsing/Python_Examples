# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:52:19 2018

@author: lankuohsing
"""
# In[]
# -*- coding: utf-8 -*-

import os
# In[]
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print("root",root) #当前目录路径
        print("dirs",dirs) #当前路径下所有子目录
        print("files",files) #当前路径下所有非目录子文件
# In[]
file_dir="."
file_name(file_dir)
