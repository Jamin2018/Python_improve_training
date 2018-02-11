# -*- coding:utf-8 -*-
'''
西班牙足球甲级联赛，每轮球员进球统计：
第一轮：{'a':1,'b':2,'c':1,'d':3...}
第一轮：{'a':2,'d':2,'e':1,'f':3...}
第一轮：{'a':1,'g':2,'f':1,'h':3...}

统计出前N轮，每场比赛都有的进球的球员
'''

def common_key():
    # 效率低
    # 生成随机字典
    from random import randint,sample   # sample随机取样
    s1 = {x:randint(1,4) for x in sample('abcdefgh',randint(3,6))}
    s2 = {x:randint(1,4) for x in sample('abcdefgh',randint(3,6))}
    s3 = {x:randint(1,4) for x in sample('abcdefgh',randint(3,6))}
    print s1,s2,s3
    res = []
    for k in s1:
        if k in s2 and k in s3:
            res.append(k)
    print res

common_key()

def set_key():
    '''利用set集合的特性'''
    # 生成随机字典
    from random import randint,sample   # sample随机取样
    s1 = {x:randint(1,4) for x in sample('abcdefgh',randint(3,6))}
    s2 = {x:randint(1,4) for x in sample('abcdefgh',randint(3,6))}
    s3 = {x:randint(1,4) for x in sample('abcdefgh',randint(3,6))}
    # 将字典转成类集合的类型
    # s1.viewkeys()
    # s2.viewkeys()
    # s3.viewkeys()
    # s = s1.viewkeys() & s2.viewkeys() & s3.viewkeys()   # 三轮
    ss = map(dict.viewkeys,[s1,s2,s3])  # 若 N 轮
    sss = reduce(lambda a,b: a & b,ss)
    # print s
    print ss
    print sss

set_key()