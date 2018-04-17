#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#@author: 时尚梦齐
from lib.base import Baseclass
from conf import settings
import json,os

class Teacher(Baseclass):
    def __init__(self,teacher_name,teacher_salary,teacher_school):
        Baseclass.__init__(self)
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_school = teacher_school

    def create_class_record(self):
        class_record = []
        student_school = input("选择学校：").strip()
        student_classes = input("选择班级：").strip()
        student_times = input("课次：").strip()
        student_list = Baseclass.open(self,"student")
        for i in student_list:
            # print(i)
            if 'pay_state' not in i:
                continue
            if i["school"] == student_school and i["classes"] == student_classes:
                student_name = i["user"]
                student_status = input("%s 上课情况：" % student_name).strip()
                # i["上课情况"].append(student_status)
                i["上课情况"] = student_status
                # student_times = input("%s 课次：" % student_name)
                # i["课次"].append(student_times)
                i["课次"] = student_times
                class_record.append(i)
        Baseclass.seek_list(self,"class_record",class_record)

    def create_class_grade(self):
        class_grade = []
        student_school = input("选择学校：").strip()
        student_classes = input("选择班级：").strip()
        student_times = input("课次：").strip()
        student_list = Baseclass.open(self,"student")
        for i in student_list:
            print(i)
            if 'pay_state' not in i:
                continue
            if i["school"] == student_school and i["classes"] == student_classes:
                student_name = i["user"]
                student_grade = input("%s 成绩：" % student_name).strip()
                i["成绩"] = student_grade
                i["课次"] = student_times
                class_grade.append(i)
        Baseclass.seek_list(self,"class_grade",class_grade)
    def teacher_view_grade(self):
        grade_list = []
        student_school = input("校名：").strip()
        student_class = input("班级：").strip()
        student_times = input("课次：").strip()
        class_grade_list = Baseclass.open(self, "class_grade")
        for i in class_grade_list:
            for j in i:
                if j["school"] == student_school and j["classes"] == student_class and j["课次"] == student_times:
                    grade_list.append(j)
        for i in grade_list:
            for key in i:
                print(key,i[key])
            print("\n")

    def tacher_view_record(self):
        record_list = []
        student_school = input("校名：").strip()
        student_class = input("班级：").strip()
        student_times = input("课次：").strip()
        class_record_list = Baseclass.open(self, "class_record")
        for i in class_record_list:
            for j in i:
                if j["school"] == student_school and j["classes"] == student_class and j["课次"] == student_times:
                    record_list.append(j)
        for i in record_list:
            for key in i:
                print(key,i[key])
            print("\n")

class Teacher_view(Teacher,):
    def __init__(self,teacher_name,teacher_salary,teacher_school):
        Teacher.__init__(self,teacher_name,teacher_salary,teacher_school)

    def auth(self,username,password):
        teacher_file = "%s/%s.json" %(settings.db_teacher,username)
        if os.path.isfile(teacher_file):
            with open(teacher_file, 'r') as f:
                admin_data = json.load(f)
            if admin_data["name"] == username and admin_data["password"] == password:
                return True
            else:
                print("用户名或密码错误")

    def interactive(self):
        menu = u'''
        ------- 欢迎进入讲师视图 ---------
            \033[32;1m1.  创建上课记录
            2.  创建学员成绩
            3.  查看学员上课记录
            4.  查看学员成绩
            5.  返回
            \033[0m'''
        menu_dic = {
            '1': Teacher.create_class_record,
            '2': Teacher.create_class_grade,
            '3': Teacher.tacher_view_record,
            '4': Teacher.teacher_view_grade,
            '5': "logout",
        }
        username = input("输入用户名:").strip()
        password = input("输入密码:").strip()
        auth = Teacher_view.auth(self,username,password)
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