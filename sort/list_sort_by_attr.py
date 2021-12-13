# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 21:59:17 2021

@author: lankuohsing
"""

class Student:
    def __init__(self, name, subject, mark):
        self.name = name
        self.subject = subject
        self.mark = mark


s1 = Student("Jack", "os", 64)
s2 = Student("Jim", "cn", 61)
s3 = Student("Pony", "se", 65)

L = [s1, s2, s3]
L.sort(key=lambda t: t.mark)
for i in range(0, len(L)):
    print(L[i].name+","+L[i].subject+","+str(L[i].mark))