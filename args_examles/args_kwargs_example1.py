# -*- coding: utf-8 -*-

def my_sum(*args, **kwargs):
    print(args)
    print(kwargs)
    result=0
    for x in args:
        result+=x
    for key,value in kwargs.items():
        result+=value
    return result

sum_result=my_sum(1,2,3,a=10,b=20,c=30)
print(sum_result)