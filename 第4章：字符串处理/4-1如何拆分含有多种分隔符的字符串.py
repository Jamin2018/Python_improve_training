# -*- coding:utf-8 -*-
'''
我们要把某个字符串依据分隔符号拆分不同的字段，该字符串包含多种不同的分隔符，例如：
s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

其中<,>,<;>,<|>,<\t>都是分隔符号，如何处理？
'''

'''
方法一：连续使用str.split()方法，每次处理一种分隔符号。
方法二：使用正则表达式的re.split()方法，一次性拆分字符串。（推荐使用）
'''
s = 'ab;cd|efg|hi,,,jkl|mn\topq;rst,uvw\txyz'
# 方法一
def mySplit(s,ds):
    res = [s]
    for i in ds:
        t = []
        res = map(lambda x:t.extend(x.split(i)),res)
        res = t
    t = [x for x in res if x]
    str4 = "".join(t)
    return str4  # 去除连续分隔符参数的空字符串

ds = ';,|\t'
print mySplit(s,ds)

# 方法二
def reSplit():
    import re
    res = re.split(r'[;,|\t]',s)
    t = [x for x in res if x]
    str4 = "".join(t)
    return str4

print reSplit()