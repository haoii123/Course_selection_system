#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#@author: 时尚梦齐
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from core import main

if __name__ == '__main__':
    a = main.Run()
    a.interactive()