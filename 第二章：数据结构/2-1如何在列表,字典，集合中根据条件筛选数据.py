# -*- coding:utf-8 -*-

from random import randint
import timeit

'''------------------------------------------'''
# 问题:过滤小于0的列表的元素
# 生成随机列表
data = [randint(-10,10) for i in range(10)]

# 通用法
# 这个最慢
def general_filter(data):
    li = []
    for i in data:
        if i >= 0:
            li.append(i)
    return li

# 函数式编程法：
def Functional_filter(data):
    new_data = filter(lambda x:x >= 0,data)   # 前一个是过滤函数
    return new_data

# 列表解析
# 这个最快
def List_filter(data):
    new_data = [i for i in data if i >=0]
    return new_data



'''------------------------------------------'''
# 问题:过滤小于0的字典的元素
# 生成随机字典
dic = {x :randint(60,100) for x in range(1,21)}

# 字典解析
def Dict_filter(dic):
    new_dic = {k:v for k,v in dic.iteritems() if v >90}
    return new_dic

# print Dict_filter(dic)

'''------------------------------------------'''
# 问题:过滤小于0的集合的元素
# 生成随机集合
s = set(data)

# 集合解析
def Set_filter(s):
    new_set = {i for i in s if i >= 0 }
    return new_set

print Set_filter(s)
