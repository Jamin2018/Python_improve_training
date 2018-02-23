# -*- coding:utf-8 -*-
'''
某编程竞赛系统，对参数选手编程解题进行计时，选手完成题目后，把该选手解题用时记录到字典中，以便赛后按选手名查询成绩。
（答题时间越短，成绩越优）
{'Lilie':(2,43),'HanMeimei':(5,52),'Jim':(1,39)...}

比赛结束后，需按排名顺序依次打印选手成绩，如何实现？
'''

'''------------------------------------------'''
# 默认无序字典
d = {}
d['Jim'] = (1,35)
d['Leo'] = (2,37)
d['Bob'] = (3,40)
# for k in d:print k
'''------------------------------------------'''
# 生成有序字典
from collections import OrderedDict
d1 = OrderedDict()
d1['Jim'] = (1,35)
d1['Leo'] = (2,37)
d1['Bob'] = (3,40)
# for k in d1:print k

def OrderedDict_filter():
    '''生成有序的字典，将先完成的人依次加入字典'''
    import time
    from random import randint
    from collections import OrderedDict
    d = OrderedDict()

    players = list('abcdefgh')
    # print players
    start_time = time.time()
    for i in range(len(players)):
        raw_input()
        p = players.pop(randint(0,7 - i))
        last_time = time.time()
        print i+1,p,last_time-start_time
        d[p]=(i+1,last_time-start_time)
    return d
d = OrderedDict_filter()
for i in d:print i,d[i]