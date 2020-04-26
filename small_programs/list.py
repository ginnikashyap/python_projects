# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:10:48 2019

@author: GINNI
"""

list1=[1,2,3]
multiplied=[item*3 for item in list1]
print (multiplied)
user_input="1,2,3,4"
user_no=user_input.split(",")
print(user_no)
user_no_as_int=[int(num) for num in user_no]
print (user_no_as_int)
