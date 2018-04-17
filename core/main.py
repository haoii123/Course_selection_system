#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#@author: 时尚梦齐
from lib.student import Student_view
from lib.teacher import Teacher_view
from lib.admin import Admin_view


class Run(object):
    def __init__(self):
        pass
    def interactive(self):
        menu = '''
            --------欢迎进入选课系统--------
            \033[32;1m1.学生视图
            2.讲师视图
            3.管理视图
            4.退出系统
            \033[0m
        '''
        menu_dic = {
            '1':Student_view,
            '2':Teacher_view,
            '3':Admin_view,
            '4':'logout'
        }
        exit_flag = False
        while not exit_flag:
            print(menu)
            option_view = input('请选择视图:').strip()
            if option_view in menu_dic:
                if option_view == '4':
                    exit_flag = True
                else:
                    menu_dic[option_view].interactive(self)
            else:
                print('\033[31;1m输入错误,请重新输入\033[0m')

