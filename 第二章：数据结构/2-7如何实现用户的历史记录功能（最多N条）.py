# -*- coding:utf-8 -*-

'''
很多应用程序都有浏览用户的历史记录功能，例如：
浏览器可以查看最近访问过的网页
视频播放器可以查看最近播放过视频文件
Shell可以查看用户输入过的命令
等等

现在我们制作了一个简单的猜数字的小游戏，添加历史记录的功能，显示用户最近猜过的数字，如何实现？
'''

import random
N = random.randint(0,100)
def guess_number(k):
    if k == N :
        print 'right'
        return True
    if k < N:
        print '%s is less-than N' % k
        return False
    else:
        print '%s is greater-than N' % k
    return False


# 使用队列记录数据
from collections import deque

# 本地记录可使用 pickle 内置函数保存Python对象
# pickle.dump(history,open('history','w'))  写入
# history2 =  pickle.load(open('history','w'))  读出
history = deque([],5)   # 建立长度为5的队列
while True:
    line = raw_input('请输入你猜测的数字：')
    if line.isdigit():
        k = int(line)
        # 入队,超过长度的自动出队
        history.append(k)
        if guess_number(k):
            break
    elif line == 'h':
        print list(history)