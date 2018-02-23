# -*- coding:utf-8 -*-
'''
有某个文本文件，我们想读取其中某范围的内容如100~300行之间的内容，Python中文本是可迭代对象，
我们是否可以使用类似列表切片的方式得到一个100~300行文件内容的生成器？

f = open('/var/log/dmesg')
f[100:300]  可以吗？
'''

from itertools import islice
# islice 会消耗原来的可迭代对象
for i in islice(u'0123456789可迭代对象',1,3):   # 区间
    print i
print '-----------------------'
for i in islice(u'0123456789可迭代对象',4,5):  # 这个不是单独第4个索引值吗？
    print i
print '-----------------------'
for i in islice(u'0123456789可迭代对象',10,None):  # 这个不是
    print i