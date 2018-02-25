# -*- coding:utf-8 -*-
'''
1.过滤掉用户输入中前后多余的空白字符：
'   nick2018@qq.com   '

2.过滤某windows下编辑文本中的'\r':
'hello world\r\n'

'''

'''
方法一：字符串strip(),lstrip(),rstrip()方法去掉字符串两端字符
方法二：删除行单个固定位置的字符，可以使用切片 + 拼接的方法
方法三：字符串的replace()方法或正则表达式re.sub()删除任意位置字符
方法四：字符串translate()方法，可以同时删除多种不用的字符
'''

# 方法一
s = '   nick2018    @qq.com   '
print s.strip()
print s.lstrip()
print s.rstrip()
s = '---abc+++'
print s.strip('+-')

# 方法二
s = 'abc:123'
print s[:3] + s[4:]

# 方法三
s = '\tabc\t123\t666'
print s.replace('\t','')

s = '\ta\rbc\t12\r3\t666\r'
import re
print re.sub('[\t\r]','',s)

# 方法四
s = 'abc1230323xyz'
import string
print s.translate(string.maketrans('abcxyz','xyzabc'))
s = '\ta\rbc\t12\r3\t666\r'
print s.translate(None,'\t\r')