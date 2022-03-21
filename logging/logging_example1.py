# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:55:55 2022

@author: lankuohsing
"""

import logging  # 引入logging模块
#logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 将信息打印到控制台上

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Log等级总开关
logging.debug("debug log")
logging.info("info log")
logging.warning("warning log")
logging.error("error log")
logging.critical("critical log")