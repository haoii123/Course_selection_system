#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#@author: 时尚梦齐
from core import uid
from conf import settings
import os,pickle,re
re_json = re.compile(r'.*json$')

class Baseclass(object):
    def __init__(self):
        pass

    def save(self,type,dict):
        filename = uid.create_md5()
        dict['uid'] = filename
        file_path = os.path.join(settings.db_DIR,type)
        ab_file = os.path.join(file_path,filename)
        if os.path.isdir(file_path):
            with open(ab_file,'wb') as f:
                f.write(pickle.dumps(dict))
                f.flush()
                if os.path.isfile(ab_file):
                    print('------%s创建成功------'%type)
                    for key in dict:
                        print(key,':\t',dict[key])

    def seek_list(self,type,list):
        filename = uid.create_md5()
        file_path = os.path.join(settings.db_DIR,type)
        ab_file = os.path.join(file_path,filename)
        if os.path.isdir(file_path):
            with open(ab_file,'wb') as f:
                f.write(pickle.dumps(list))
                f.flush()
                if os.path.isfile(ab_file):
                    print('------%s创建成功------'%type)
                    for i in list:
                        for key in i:
                            print(key,':\t',i[key])
                        print('\n')
        # return True

    def open(self,type):
        all_data = []
        db_path = os.path.join(settings.db_DIR,type)
        for i in os.listdir(db_path):
            # print("==============>",i)
            if re_json.search(i):
                continue
            if os.path.isfile(os.path.join(db_path,i)):
                db_file = os.path.join(db_path,i)
                with open(db_file,'rb') as f:
                    file_dict = pickle.load(f)
                    all_data.append(file_dict)
        return all_data

    def modify(self,type,dict):
        filename = dict['uid']
        file_path = os.path.join(settings.db_DIR,type)
        ab_file = os.path.join(file_path,filename)
        if os.path.isdir(file_path):
            with open(ab_file,'wb') as f:
                f.write(pickle.dumps(dict))
                f.flush()
                if os.path.isfile(ab_file):
                    print('------%s修改成功------'%type)
                    for key in dict:
                        print(key,':\t',dict[key])