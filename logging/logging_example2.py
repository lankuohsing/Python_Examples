# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:34:06 2022

@author: lankuohsing
"""

import logging  # 引入logging模块
"""
https://blog.csdn.net/colinlee19860724/article/details/90965100
"""
logging.basicConfig(level=logging.NOTSET,#CRITICAL > ERROR > WARNING()默认 > INFO > DEBUG
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a %d %b %Y %H:%M:%S',
                    filename='./my.log',#windows下在CMD里运行才会生成文件和添加日志内容
                    filemode='a')#w：清除历史内容写入新内容；a：追加内容
logging.debug("This debug log")
logging.info("This info log")
logging.warning("This warning log")
logging.error("This error log")
logging.critical("This critical log")