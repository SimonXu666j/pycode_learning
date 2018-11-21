#-*-coding:utf-8
#如何拆分含有多种分隔符的字符串？
'''
    方法一：连续使用str.split()方法，每次处理一种分隔符
    方法二：使用正则表达式的re.split()方法，一次性拆分字符串
'''
import re
s='ab;s;3;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
s_change=re.split(r'[,;\t|]+',s)
print(s_change)