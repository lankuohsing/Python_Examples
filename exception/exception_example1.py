# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:13:02 2022

@author: lankuohsing
"""

person_info={"Name":"Jack","Age":20,"Gender":"Male"}
try:
#    a=1/0
    print(person_info["Weight"])
except Exception as e:
    print("Exception happens! ",repr(e))#repr(e)的信息比较全；如果是str(e)则打印信息不全
print(person_info["Age"])
print(person_info["Gender"])



# In[]
person_info={"Name":"Jack","Age":20,"Gender":"Male","Weight":10,"Height":0}
try:
    print(person_info["Weight"])
    print(person_info["Height"])
    BMI=person_info["Weight"]/(person_info["Height"])
except KeyError:
    print("Key Weight doesn't exist!")
except ZeroDivisionError:
    print("Divided by Height but Height is zero!")
print(person_info["Age"])
print(person_info["Gender"])


# In[]
s = "123"
try:
    if s is None or s=="123":#试试把s=="123"去掉
        print("s 是空对象 or s==123")
        # 未声明/初始化对象 (没有属性)
        raise NameError     #如果引发NameError异常，后面的代码将不能执行
    print(len(s))
except NameError:
    print("空对象没有长度")
else:
    print(len(s),"again")
print(111)

"""
s 是空对象 or s==123
空对象没有长度
111
"""