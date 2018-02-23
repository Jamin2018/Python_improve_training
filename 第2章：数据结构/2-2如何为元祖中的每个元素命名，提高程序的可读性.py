# -*- coding:utf-8 -*-

# ('Jim',16,'male','jim8752@mail.com')
# ('LiLei',17,'male','leili@qq.com')
# ('Lucy',16,'female','lucy123456@yahoo.com')

'''------------------------------------------'''
# 基础查询
def general_method():
    student = ('Jim',16,'male','jim8752@mail.com')
    # name
    print student[0]
    # age
    print student[1]
    # sex
    if student[2] == 'male':
        pass

'''------------------------------------------'''
# 类枚举方法
def Meiju_method():
    NAME,AGE,SEX,MAIL = 0,1,2,3
    student = ('Jim', 16, 'male', 'jim8752@mail.com')
    print student[NAME]
    print student[AGE]
    print student[SEX]
    print student[MAIL]
# Meiju_method()
'''------------------------------------------'''
# 内置库
# 开销仅大一点
def neizhiku_method():
    from collections import namedtuple
    Student = namedtuple('Student',['NAME','AGE','SEX','MAIL'])
    s = Student('Jim', 16, 'male', 'jim8752@mail.com')
    print s
    print s.NAME
    print s.AGE
    print s.SEX
    print s.MAIL
neizhiku_method()