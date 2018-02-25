# -*- coding:utf-8 -*-
'''
某文件系统目录下有一系列文件：
quicksort.c
graph.py
heap.java
install.sh
stack.cpp

编写程序给其中所有.sh文件和.py文件加上用户可执行权限
'''

'''
解决方案：使用字符串的str.startswith()和str.endswith()方法.
        注意：多个匹配时参数使用元组.
'''
import os,stat

t = []
for name in os.listdir('.'):
    if name.endswith(('.sh','.c')):
        t.append(name)

t1 = [name for name in os.listdir('.') if name.endswith(('.sh','.c'))]


print oct(os.stat('quicksort.c').st_mode)
os.chmod('quicksort.c',os.stat('quicksort.c').st_mode | stat.S_IXUSR)
print oct(os.stat('quicksort.c').st_mode)