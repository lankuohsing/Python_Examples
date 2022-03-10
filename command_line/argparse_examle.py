# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:28:26 2022

@author: lankuohsing
"""

import argparse


parser = argparse.ArgumentParser(description="Demo of argparse")
parser.add_argument('-n','--name', default=' lankuohsing ')
parser.add_argument('-y','--year', default='20')
args = parser.parse_args()
print(args)
a = args.name
b = args.year

print(type(a))
print(a+b)
