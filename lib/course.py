#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#@author: 时尚梦齐
from lib.base import Baseclass

class Course(Baseclass):
    def __init__(self,course_name,course_period,course_prices):
        Baseclass.__init__(self)
        self.course_name = course_name
        self.course_period = course_period
        self.course_prices = course_prices