#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: 时尚梦齐
from lib.base import Baseclass


class Student(Baseclass):
    student_dic = {}

    def __init__(self, student_name, student_gender, student_school, student_classes):
        super().__init__()
        self.student_name = student_name
        self.student_gender = student_gender
        self.student_school = student_school
        self.student_classes = student_classes
        self.student_dic = Student.student_dic

    def student_info(self, dict):
        for key in dict:
            print(key, ':', dict[key])

    def student_pay(self, dict):
        if 'pay_state' not in dict.keys():
            school_list = Baseclass.open(self, 'school')
            classes_list = Baseclass.open(self, 'classes')
            course_list = Baseclass.open(self, 'course')
            teacher_list = Baseclass.open(self, 'teacher')
            for i in school_list:
                for j in classes_list:
                    for k in course_list:
                        for g in teacher_list:
                            if g['所属学校'] == i['校名'] and g['姓名'] == j['负责讲师'] \
                                    and j['课程'] == k['课程名']:
                                print('校名:', i['校名'], '地址:', i['地址'], '班级:', j['班级名'], \
                                      '课程:', k['课程名'], '周期:', k['周期'], '价格:', k['价格'], '讲师:', j['负责讲师'])

            student_school = input('输入学校')
            student_classes = input('输入班级')
            student_course = input('输入课程')
            student_course_period = input('输入缴费金额')
            for i in course_list:
                if student_course == i['课程名'] and student_course_period == i['价格']:
                    print('报名成功')
            dict['school'] = student_school
            dict['classes'] = student_classes
            dict['course'] = student_course
            dict['pay_state'] = True
            Baseclass.modify(self, 'student', dict)
        else:
            print(dict['user'], '只能报一门课')

    def student_class_record(self, dict):
        class_record_list = Baseclass.open(self,'class_record')
        for i in class_record_list:
            for j in i:
                if j['uid'] == dict['uid']:
                    for g in j:
                        print(g,':',j[g])

    def student_class_grade(self, dict):
        class_grade_list = Baseclass.open(self, 'class_grade')
        for i in class_grade_list:
            for j in i:
                if j['uid'] == dict['uid']:
                    for g in j:
                        print(g,':',j[g])

class Student_view(Student):
    def __init__(self, student_user, student_pwd):
        super().__init__()
        self.student_user = student_user
        self.student_pwd = student_pwd

    def student_register(self):
        student_dict = {}
        username = input("请输入用户名:").strip()
        student_list = Baseclass.open(self, 'student')
        for i in student_list:
            if i['user'] == username:
                print('用户%s已注册' % username)
                Student_view.interactive(self)
        password1 = input("请输入密码:").strip()
        password2 = input("请再次输入密码:").strip()
        if password1 == password2:
            user = username
            pwd = password1
            std1 = Student_view(user, pwd)
            student_dict['user'] = std1.student_user
            student_dict['pwd'] = std1.student_pwd
            Baseclass.save(self, 'student', student_dict)
        else:
            print('两次密码不一致')
            Student_view.interactive(self)

    def student_login(self):
        username = input("请输入用户名:").strip()
        password = input("请输入密码:").strip()
        student_list = Baseclass.open(self, 'student')
        for i in student_list:
            if i['user'] == username and i['pwd'] == password:
                menu = '''
                            \033[32;1m1.学员信息
                            2.报名缴费
                            3.查看上课记录
                            4.查看成绩
                            5.返回\033[0m
                        '''
                menu_dic = {
                    '1': Student.student_info,
                    '2': Student.student_pay,
                    '3': Student.student_class_record,
                    '4': Student.student_class_grade,
                    '5': 'logout'
                }
                exit_flag = False
                while not exit_flag:
                    print(menu)
                    option = input('请选择:').strip()
                    if option in menu_dic:
                        if option == '5':
                            exit_flag = True
                        else:
                            menu_dic[option](self, i)
                    else:
                        print('\033[31;1m输入错误，重新输入\033[0m')

    def interactive(self):
        menu = '''
            \033[32;1m1.注册
            2.登录
            3.返回\033[0m
        '''
        menu_dic = {
            '1': Student_view.student_register,
            '2': Student_view.student_login,
            '3': 'logout'
        }
        exit_flag = False
        while not exit_flag:
            print(menu)
            option = input('请选择:').strip()
            if option in menu_dic:
                if option == '3':
                    exit_flag = True
                else:
                    menu_dic[option](self)
            else:
                print('\033[31;1m输入错误，重新输入\033[0m')
