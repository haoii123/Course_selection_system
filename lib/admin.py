#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#@author: 时尚梦齐
from lib.base import Baseclass
from lib.school import School
from lib.teacher import Teacher
from lib.student import Student
from lib.course import Course
from lib.classes import Classes
from conf import settings
import json,os
class Admin(Baseclass):
    def __init__(self):
        Baseclass.__init__(self)
    def create_school(self):
        school_dict = {}
        school_name = input("校名：")
        school_address = input("地址：")
        s1 = School(school_name, school_address)
        school_dict["校名"] = s1.school_name
        school_dict["地址"] = s1.school_address
        Baseclass.save(self, "school", school_dict)
    def create_teacher(self):
        teacher_dict = {}
        teacher_name = input("讲师姓名：")
        teacher_salary = input("讲师工资：")
        teacher_school = input("所属学校：")
        t1 = Teacher(teacher_name, teacher_salary, teacher_school)
        teacher_dict["姓名"] = t1.teacher_name
        teacher_dict["工资"] = t1.teacher_salary
        teacher_dict["所属学校"] = t1.teacher_school
        print(teacher_dict)
        Baseclass.save(self, "teacher", teacher_dict)
    def create_student(self):
        student_dict = {}
        student_name = input("学员姓名：")
        student_sex = input("学员性别：")
        student_school = input("所属学校：")
        student_classes = input("学员班级：")
        st1 = Student(student_name, student_sex, student_school, student_classes)
        student_dict["姓名"] = st1.student_name
        student_dict["性别"] = st1.student_sex
        student_dict["学校"] = st1.student_school
        student_dict["班级"] = st1.student_classes
        Baseclass.save(self, "student", student_dict)
    def create_course(self):
        course_dict = {}
        course_name = input("课程名：")
        course_period = input("周期：")
        course_prices = input("价格：")
        c1 = Course(course_name, course_period, course_prices)
        course_dict["课程名"] = c1.course_name
        course_dict["周期"] = c1.course_period
        course_dict["价格"] = course_prices
        Baseclass.save(self, "course", course_dict)
    def create_classes(self):
        classes_dict = {}
        classes_name = input("班级名：")
        classes_teachter = input("负责讲师：")
        classes_course = input("所学课程：")
        cs1 = Classes(classes_name, classes_teachter, classes_course)
        classes_dict["班级名"] = cs1.classes_name
        classes_dict["负责讲师"] = cs1.classes_teacher
        classes_dict["课程"] = cs1.classes_course
        Baseclass.save(self, "classes", classes_dict)

class Admin_view(Admin):
    def __init__(self):
        Admin.__init__(self)
    def auth(self,username,password):
        admin_file = "%s/%s.json" %(settings.db_admin,username)
        if os.path.isfile(admin_file):
            with open(admin_file, 'r') as f:
                admin_data = json.load(f)
            if admin_data["name"] == username and admin_data["password"] == password:
                return True
            else:
                print("用户名或密码错误")
    def interactive(self):
        menu = u'''
        ------- 欢迎进入管理视图 ---------
            \033[32;1m 1.  校区管理
            2.  讲师管理
            3.  学员管理
            4.  课程管理
            5.  返回
            \033[0m'''
        menu_dic = {
            '1': Admin_view.school_manager,
            '2': Admin_view.teacher_manager,
            '3': Admin_view.student_manager,
            '4': Admin_view.course_manager,
            '5': "logout",
        }
        username = input("输入用户名:").strip()
        password = input("输入密码:").strip()
        auth = Admin_view.auth(self,username,password)
        if auth:
            exit_flag = False
            while not exit_flag:
                print(menu)
                option = input("请选择：").strip()
                if option in menu_dic:
                    if int(option) == 5:
                        exit_flag = True
                    else:
                        # print(menu_dic[option])
                        menu_dic[option](self)
                else:
                    print("\033[31;1m输入错误，重新输入\033[0m")
    def school_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入校区管理 ---------
                \033[32;1m1.  创建校区
                2.  创建班级
                3.  返回
                \033[0m
            """)
            option = input("请选择：").strip()
            if int(option) == 1:
                Admin.create_school(self)
            elif int(option) == 2:
                Admin.create_classes(self)
            else:
                exit_flag = True
    def teacher_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入讲师管理 ---------
                \033[32;1m 1.  创建讲师
                2.  ...
                3.  返回
                \033[0m
            """)
            option = input("请选择：").strip()
            if int(option) == 1:
                Admin.create_teacher(self)
            elif int(option) == 2:
                print("扩展中")
            else:
                exit_flag = True

    def student_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入学员管理 ---------
                \033[32;1m 1.  创建学员
                2.  ...
                3.  返回
                \033[0m
            """)
            option = input("请选择：").strip()
            if int(option) == 1:
                Admin.create_student(self)
            elif int(option) == 2:
                print("扩展中")
            else:
                exit_flag = True
    def course_manager(self):
        exit_flag = False
        while not exit_flag:
            print("""
                ------- 欢迎进入课程管理 ---------
                \033[32;1m 1.  创建课程
                2.  ...
                3.  返回
                \033[0m
            """)
            option = input("请选择：").strip()
            if int(option) == 1:
                Admin.create_course(self)
            elif int(option) == 2:
                print("扩展中")
            else:
                exit_flag = True