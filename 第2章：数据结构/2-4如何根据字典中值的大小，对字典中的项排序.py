# -*- coding:utf-8 -*-

# 某班英语成绩已字典形式储存为：{'Lilei':79,'Jim':88},'Lucy':92...},根据成绩高低，计算学生排名。

def sorted_filter():
    # 随机生成成绩字典
    from random import randint
    dic = {x:randint(60,100) for x in 'abcdefg'}
    new_dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    print dic
    print dic.items()
    print new_dic
sorted_filter()