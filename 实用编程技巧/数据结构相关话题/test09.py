#-*-coding:utf-8-*-
# 如何快速找到多个字典中的公共键(key)？
# 利用集合set的交集操作
'''
    1.使用字典的viewkeys()方法，得到一个字典keys的集合
    2.使用map函数，得到所有字典的keys的集合
    3.使用reduce函数，取所有字典的keys的集合的交集
    该脚本在python2.x环境执行
'''
from random import randint,sample
from functools import reduce
li=sample('abcdedfg',randint(3,6))
s1={x:randint(1,4) for x in sample('abcdedfg',randint(3,6))}
# print(s1)
s1={x:randint(1,4) for x in sample('abcdedfg',randint(3,6))}
s2={x:randint(1,4) for x in sample('abcdedfg',randint(3,6))}
s3={x:randint(1,4) for x in sample('abcdedfg',randint(3,6))}
# 1.使用字典的viewkeys()方法，python3.x只有keys()方法，python2.x中keys()返回的是列表，得到一个字典keys的集合
# print(s1.viewkeys() & s2.viewkeys() & s3.viewkeys())
# print(s1.keys() & s2.keys() & s3.keys())
# 2.使用map函数，得到所有字典的keys的集合
# 3.使用reduce函数，取所有字典的keys的集合的交集
# print(map(dict.keys,[s1,s2,s3]))
print(reduce(lambda a,b:a & b,map(dict.viewkeys,[s1,s2,s3])))