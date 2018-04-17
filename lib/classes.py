#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#@author: 时尚梦齐
from lib.base import Baseclass

class Classes(Baseclass):
    def __init__(self,classes_name,classes_teachter,classes_course):
        Baseclass.__init__(self)
        self.classes_name = classes_name
        self.classes_teacher = classes_teachter
        self.classes_course = classes_course