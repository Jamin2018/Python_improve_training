# -*- coding:utf-8 -*-

# 1.某随机序列[12,4,5,6,3,4,8,12,4,62,3,...]中，找到出现次数最高的三个元素，它们出现次数是多少
# 2.对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，它们出现次数是多少？

'''------------------------------------------'''
from random import randint
# 生成列表
data = [randint(0,10) for i in range(100)]

def general_number(data):
    # dict = {data:count_number}
    # 类计数排序
    dic = dict.fromkeys(data,0)
    for i in data:
        dic[i] += 1
    new_dic = sorted(dic.items(),key=lambda x:x[1])
    print dic
    print new_dic[-3:]

general_number(data)
'''------------------------------------------'''
# 内置函数
def neizhihanshu_number(data):
    from collections import Counter
    c = Counter(data)
    print c
    print c.most_common(3)

neizhihanshu_number(data)
