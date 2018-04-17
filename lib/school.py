#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#@author: 时尚梦齐
from lib.base import Baseclass

class School(Baseclass):
    def __init__(self,school_name,school_address):
        Baseclass.__init__(self)
        self.school_name = school_name
        self.school_address = school_address