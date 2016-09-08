# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:55:23 2016

@author: yuxitao
"""
from classTest import Test
class human:
    age = 0
    sex = ''
    height = 0
    weight = 0
    name = ''

class student(human):
    school = ''
    number = 0
    grade = 0
    
class book:
    __author = ''
    __name = ''
    pages = 0
    price= 0
    press = ''
    
    def __init__(self,author,name):
        self.__author = author
        self.__name = name
        
    def show(self):
        print( self.__author)
        print (self.__name)
#    def show(self,name):
#        print('only name'+name)
        
    def setname(self,name):
        self.__name = name
        
        
##########################################    
a = book('Yu','Programming Java')
a.setname('yuxitao')
print(a.show())
b = Test()
b.allprint()