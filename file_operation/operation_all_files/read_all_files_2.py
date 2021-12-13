# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:04:07 2018

@author: lankuohsing
"""
"""
递归地获取某一个目录下所有子目录里面的所有文件的路径名称，文件路径名称包括了文件名和它的上面的路径名
"""
# -*- coding: utf-8 -*-
# In[]
import os

def listdir(path, list_name):  #传入存储的list
    for file in os.listdir(path):
        print("file",file)
#        file_path = os.path.join(path, file)
        file_path=os.path.join(path,file)#注意：在windows下，路径分割符为"\"，但在代码中表示它时，要加上转义符号"\"
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)
# In[]
path="."
list_name=[]
listdir(path, list_name)
