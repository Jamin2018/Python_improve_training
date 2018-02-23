# -*- coding:utf-8 -*-
'''
实现一个连续浮点数发生器FloatRange(和xrange类似)，根据给定范围(start,end)和步进值(step)产生一些列连续
浮点数，如迭代FloatRange(3.0,4.0,0.2) 可产生序列：

正向：3.0 - 3.2 - 3.4 - 3.6 - 3.8 - 4.0
反向：4.0 - 3.8 - 3.6 - 3.4 - 3.2 - 3.0
'''

# # 反向迭代器  类似 iter(l)
# l = [1,2,3,4,5]
# for i in reversed(l):
#     print i

class FloatRange:
    def __init__(self,start,end,step=0.1):
        self.start = start
        self.end = end
        self.step = step

    # 正向迭代器
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step
    # 反向迭代器
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

for i in FloatRange(3.0,4.0,0.5):
    print i