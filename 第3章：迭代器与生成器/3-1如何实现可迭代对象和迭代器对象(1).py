# -*- coding:utf-8 -*-
'''
某软件要求，从网络抓取各个城市气温信息，并依次显示：
北京：15~20
天津：17~22
长春：12~18
...

如果一次抓取所有城市天气再显示，显示第一个城市气温时，有很高的延时，并且浪费储存空间。
我们期望以‘用时访问’的策略，并且能把所有城市气温封装到一个对象里，可用for语句进行迭代，如何解决？
'''

l = [1,2,3,4,5]
s = iter(l)
print s.next()
print s.next()
