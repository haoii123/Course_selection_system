#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#@author: 时尚梦齐
import time,hashlib

def create_md5():
    m = hashlib.md5()
    m.update(bytes(str(time.time()),encoding='utf-8'))
    return m.hexdigest()