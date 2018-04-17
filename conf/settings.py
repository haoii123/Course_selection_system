#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#@author: 时尚梦齐
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# sys.path.append(BASE_DIR)
# sys.path.insert(0,Base_Dir)

db_DIR = os.path.join(BASE_DIR,'db')
db_admin = os.path.join(db_DIR,'admin')
db_class_grade = os.path.join(db_DIR,'class_grade')
db_class_record = os.path.join(db_DIR,'class_record')
db_classes = os.path.join(db_DIR,'classes')
db_course = os.path.join(db_DIR,'course')
db_school = os.path.join(db_DIR,'school')
db_student = os.path.join(db_DIR,'student')
db_teacher = os.path.join(db_DIR,'teacher')

