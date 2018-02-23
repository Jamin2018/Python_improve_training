# -*- coding:utf-8 -*-
'''
1.某班学生期末考试成绩，语文，数学，英语分别储存在3个列表中，同时迭代三个代表，计算每个学生的总分。（并行）
解决方案：使用内置函数zip，它能将多个可迭代对象合并，每次返回一个元组。

2.某年级有4个班，某次考试每班英语成绩分别储存在4个列表中，依次迭代每个列表，统计全学年成绩高于90分人数。（串行）
解决办法：使用标准库中的itertools.chain,它能将多个可迭代对象连接。

'''

from random import randint

chinese = [randint(60,100) for i in xrange(40)]
math = [randint(60,100) for i in xrange(40)]
english = [randint(60,100) for i in xrange(40)]


# 1.某班学生期末考试成绩，语文，数学，英语分别储存在3个列表中，同时迭代三个代表，计算每个学生的总分。（并行）
# 最原始的，有些数据不支持索引，就用 zip 合并
# for i in xrange(len(chinese)):
#     s = chinese[i] + math[i] + english[i]
#     print s

# 1.某班学生期末考试成绩，语文，数学，英语分别储存在3个列表中，同时迭代三个代表，计算每个学生的总分。（并行）
for a,b,c in zip(chinese,math,english):
    # total = s[0]+s[1]+s[2]
    total = a + b + c
    # print total

# 2.某年级有4个班，某次考试每班英语成绩分别储存在4个列表中，依次迭代每个列表，统计全学年成绩高于90分人数。（串行）
from itertools import chain
for x in chain(chinese,math,english):
    if x > 90:print x